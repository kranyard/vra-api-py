$vRAUsername="jason@corp.local"
$vRAPassword="VMware1!"
$vRADefaultTenant="vsphere.local"
$VRA="vra-01a.corp.local"

$catalogItem = $args[0]

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
 
[ServerCertificateValidationCallback]::Ignore();

$credentials=@{username=$vRAUsername;password=$vRAPassword;tenant=$vRADefaultTenant}
############# Get Auth token ###############
$headers=@{
 "Accept"="application/json"
}
$result = Invoke-RestMethod -Uri "https://$($VRA)/identity/api/tokens" -Method Post -Headers $headers -ContentType application/json -Body (ConvertTo-Json $credentials) 

$Global:id = $result | select -ExpandProperty id
#Write-Host $id

$headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"; "Authorization" = "Bearer ${id}"}

$url = "https://$($VRA)/release-management-service/api/release-pipelines"

$pipelines = Invoke-RestMethod -Method GET -URI $url -headers $headers -ContentType application/json

write-host $pipelines.content
