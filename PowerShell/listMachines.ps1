Param (
	[string]$UserName="jason@corp.local",
	[string]$Tenant="vsphere.local",
	[string]$HostName ="vra-01a.corp.local",
    [string]$OutputFile = "machines.csv",
    [string]$Owner="jason@corp.local",
    [string]$PageSize = 20
)

$credentials = Get-Credential -UserName $UserName -Message "Enter password"
$PassWord = $credentials.GetNetworkCredential().Password
#$PassWord = "VMware1!"

$e=$ErrorActionPreference
$ErrorActionPreference='SilentlyContinue'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

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


$credentials=@{username=$UserName;password=$PassWord;tenant=$Tenant}
############# Get Auth token ###############
$headers=@{
 "Accept"="application/json"
}
$result = Invoke-RestMethod -Uri "https://$($HostName)/identity/api/tokens" -Method Post -Headers $headers -ContentType application/json -Body (ConvertTo-Json $credentials) 

$Global:id = $result | select -ExpandProperty id
#Write-Host $id

$headers = @{"Content-Type" = "application/json"; "Accept" = "application/json"; "Authorization" = "Bearer ${id}"}

$url = "https://$($HostName)/catalog-service/api/consumer/resources?`$filter=resourceType/name`%20eq`%20'Deployment'&limit=$PageSize"
# Use this URL if you only want to display machines with specific owner
#$url = "https://$($HostName)/catalog-service/api/consumer/resources?`$filter=owners/ref%20eq%20'$owner'%20and%20resourceType/name`%20eq`%20'Deployment'&limit=$PageSize"

$machines = @()

while ( $url -ne "" ) {

	$result = Invoke-RestMethod $url -Method GET -headers $headers
	
	$result.content | ForEach-Object {

		$id = $_ | select -expand id 
		
		$parent = $_
		
		$owner = $parent.owners[0].ref
		
		$url = "https://$($HostName)/catalog-service/api/consumer/resources?`$filter=parentResource/id`%20eq`%20'${id}'"
		
		$iresult = Invoke-RestMethod $url -Method GET -headers $headers

		$iresult.content | where { $_.resourceTypeRef.label -eq "Virtual Machine" } | ForEach-Object {
			
			$_ | select -expand resourceData | ForEach-Object {
				$ipAddress = $_.entries | where { $_.key -eq "ip_address" } | select -expand value | select -expand value
				$machineStatus = $_.entries | where { $_.key -eq "MachineStatus" } | select -expand value | select -expand value
				$machineMemory = $_.entries | where { $_.key -eq "MachineMemory" } | select -expand value | select -expand value
				$machineBlueprintName = $_.entries | where { $_.key -eq "MachineBlueprintName" } | select -expand value | select -expand value
				$machineReservationName = $_.entries | where { $_.key -eq "MachineReservationName" } | select -expand value | select -expand value
			}

			Write-Host ("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}" -f $_.name, $parent.name, $owner, $machineBlueprintName, $machineReservationName, $ipAddress, $machineMemory, $machineStatus)
	
            $machines += New-Object -TypeName psobject -Property @{Owner=$owner ;MachineName=$_.name;Component=$parent.name; Blueprint=$machineBlueprintName; Reservation=$machineReservationName;IPAddress =$ipAddress;Memory=$machineMemory;Status=$machineStatus}
		}
		
	}
	
	$url = ""
	$result.links | ForEach-Object {
		if ($_.rel -eq "next" ) {
			$url = $_.href
		}
	}
	
}

$machines | select MachineName, Component, Owner, Blueprint, Reservation, IPAddress, Memory, Status | Export-Csv -Path $OutputFile -NoTypeInformation