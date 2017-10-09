$vRAUsername="jason@corp.local"
$vRAPassword="VMware1!"
$vRADefaultTenant="vsphere.local"
$VRA="vra-01a.corp.local"

$itemname = $args[0]
#$itemname = "dev-0023"


Add-Type @"
    using System;
    using System.Net;
    using System.Net.Security;
    using System.Security.Cryptography.X509Certificates;
    public class ServerCertificateValidationCallback
    {
        public static void Ignore()
        {
            ServicePointManager.ServerCertificateValidationCallback += 
                delegate
                (
                    Object obj, 
                    X509Certificate certificate, 
                    X509Chain chain, 
                    SslPolicyErrors errors
                )
                {
                    return true;
                };
        }
    }
"@

[ServerCertificateValidationCallback]::Ignore() ;

 
$credentials=@{username=$vRAUsername;password=$vRAPassword;tenant=$vRADefaultTenant}
############# Get Auth token ###############
$headers=@{
 "Accept"="application/json"
}
$result = Invoke-RestMethod -Uri "https://$($VRA)/identity/api/tokens" -Method Post -Headers $headers -ContentType application/json -Body (ConvertTo-Json $credentials) 

$Global:id = $result | select -ExpandProperty id
#Write-Host $id

$headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"; "Authorization" = "Bearer ${id}"}

$url = "https://$($VRA)/catalog-service/api/consumer/resources?`$filter=name`%20eq`%20'$itemname'"
$result = Invoke-RestMethod $url -Method GET -headers $headers

$requestId = $result.content.requestId
$requestId

$url = "https://$($VRA)/catalog-service/api/consumer/requests/$($requestId)/resourceViews"
$result = Invoke-RestMethod $url -Method GET -headers $headers

$templateURL = $result.content.links | ? {$_.rel -like "GET*virtual.Destroy*"} | select -ExpandProperty href

$postURL = $result.content.links | ? {$_.rel -like "POST*virtual.Destroy*"} | select -ExpandProperty href

$template = Invoke-WebRequest $templateURL -Method GET -headers $headers

$result = Invoke-WebRequest $postURL -Method POST -headers $headers -body $template.Content

$result.StatusCode








