$vRAUsername="jason@corp.local"
$vRAPassword="VMware1!"
$vRADefaultTenant="vsphere.local"
$VRA="vra-01a.corp.local"

#$itemname = $args[0]
$itemname = "dev-0022"

$e=$ErrorActionPreference
$ErrorActionPreference='SilentlyContinue'
if (![ServerCertificateValidationCallback]) {
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
}
[ServerCertificateValidationCallback]::Ignore() ;
$ErrorActionPreference=$e
 
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

#$result.content | select name, id


$this_id = $result.content.id

$parent = $result.content.parentResourceRef
$parent_id = $parent.id

$tenantLabel=$result.content.organization.tenantLabel
$tenantRef=$result.content.organization.tenantRef
$subtenantLabel=$result.content.organization.subtenantLabel
$subtenantRef=$result.content.organization.subtenantRef

$url = "https://$($VRA)/catalog-service/api/consumer/resources/$parent_id/actions"
$result = Invoke-RestMethod $url -Method GET -headers $headers

write-host $parent.label
$result.content | select name

$url = "https://$($VRA)/catalog-service/api/consumer/resources/$this_id/actions"
$result = Invoke-RestMethod $url -Method GET -headers $headers

write-host $itemname
$result.content | select name

