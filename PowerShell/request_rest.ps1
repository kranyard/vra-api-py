$vRAUsername="jason@corp.local"
$vRAPassword="VMware1!"
$vRADefaultTenant="vsphere.local"
$VRA="vra-01a.corp.local"

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
Write-Host $id

$headers = @{"Accept" = "application/json"}
$headers.Add("Authorization", "Bearer $id")

$result = Invoke-RestMethod -Method GET -URI "https://$($VRA)/catalog-service/api/consumer/entitledCatalogItemViews" -headers $headers -ContentType application/json

$result.content |select name,catalogItemId

$selectId=$result.content | where-object {$_.name -eq "CentOS Test"} | select -ExpandProperty catalogItemId

write-host $selectId

$headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"; "Authorization" = "Bearer ${id}"}

$template = Invoke-WebRequest -Method GET -URI "https://$($VRA)/catalog-service/api/consumer/entitledCatalogItems/$($selectId)/requests/template" -headers $headers

write-host $template

$result = Invoke-WebRequest -Method POST -URI "https://$($VRA)/catalog-service/api/consumer/entitledCatalogItems/$($selectId)/requests" -headers $headers -Body $template.content

write-host $result
