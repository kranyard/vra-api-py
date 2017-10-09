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

$pipeline_params = @{
    description = 'Call from Powershell'
	pipelineParams = @( @{ name = 'BUILD_NUMBER' ; type = 'STRING' ; value = '11'} )
}

$headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"; "Authorization" = "Bearer ${id}"}

$pipeline = Invoke-RestMethod -Method GET -URI "https://$($VRA)/release-management-service/api/release-pipelines?name=ResetDemo" -headers $headers -ContentType application/json

write-host $pipeline.content.name, $pipeline.content.id

$pipeline_id = $pipeline.content.id

$url = "https://$($VRA)/release-management-service/api/release-pipelines/$($pipeline_id)/executions"
$param_json = ConvertTo-Json $pipeline_params

pause

$exec = Invoke-RestMethod -Method POST -URI $url -Body (ConvertTo-Json $pipeline_params) -Headers $headers -ContentType application/json
write-host $exec

$status = Invoke-RestMethod -Method GET -URI $url -Headers $headers -ContentType application/json
write-host $status