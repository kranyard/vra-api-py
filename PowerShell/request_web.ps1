    $vraServer = "vra-01a.corp.local"
    $catalogItem = "CentOS Test"
    $username = "jason@corp.local"
    $password = "VMware1!"
    $tenant = "vsphere.local"

	
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
	
    $url = "https://$($vraServer)/identity/api/tokens"

    $properties = @{username= $username; password = $password; tenant = $tenant}
	
    
    $body = $properties | ConvertTo-Json

    $headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"}

    $request = Invoke-WebRequest $url -Method POST -Headers $headers -Body $body
    $content = $request.content | convertFrom-json
    $bearerToken = $content.id

	
    $url = "https://$($vraServer)/catalog-service/api/consumer/entitledCatalogItems/"
    $headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"; "Authorization" = "Bearer ${bearerToken}"}
    $request = Invoke-WebRequest $url -Method GET -Headers $headers
    $content = $request.Content | ConvertFrom-Json
	
    $consumerEntitledCatalogItem = $content.content | ? { $_.catalogItem.name -eq $catalogItem }
    $consumerEntitledCatalogItemId = $consumerEntitledCatalogItem.catalogItem.id
	
    $url = "https://$($vraServer)/catalog-service/api/consumer/entitledCatalogItemViews/$($consumerEntitledCatalogItemId)"
    $request = Invoke-WebRequest $url -Method GET -Headers $headers
    $content = $request.Content | ConvertFrom-Json
	
	write-host $content 
	
    $requestTemplateURL = $content.links | ? { $_.rel -eq 'GET: Request Template' }
    $requestPOSTURL = $content.links | ? { $_.rel -eq 'POST: Submit Request' }
	
    $request = Invoke-WebRequest $requestTemplateURL.href -Method GET -Headers $headers
	
    $request = Invoke-WebRequest $requestPOSTURL.href -Method POST -Headers $headers -body $request.content
	
	$req_id = (convertFrom-json $request.Content).id
	
	write-host $req_id
	
	while ($true) {
	
		$url = "https://$($vraServer)/catalog-service/api/consumer/requests/$($req_id)"
	
		$request = Invoke-WebRequest $url -Method GET -Headers $headers
    
		$content = $request.Content | ConvertFrom-Json
	
		write-host $content.phase
		
		if ( $content.phase -eq "SUCCESSFUL" ) {
			break 
		}
	
		sleep 10
		
	}
	
	$url = "https://$($vraServer)/catalog-service/api/consumer/requests/$($req_id)/resourceViews"
	
	$request = Invoke-WebRequest $url -Method GET -Headers $headers
    
	$req = $request.Content | ConvertFrom-Json
	
	$req.content.data
	
	pause