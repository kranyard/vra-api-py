#!/usr/bin/env python
import operator
import os
import sys
import json

import rw

y = json.dumps({ "requestData": { "entries": [ { "key": "var123", "value": { "type": "string", "value": "1" } },{ "key": "var345", "value": { "type": "string", "value": "2" } } ] } })

b = json.loads(y)

e = b['requestData']['entries']


#for i in e:
	#print i['key'], i['value']['value']






#r = json.dumps( { "id": "aec4e7e3-1e7a-433a-9817-6aff478d20d9", "iconId": "Infrastructure.CatalogItem.Machine.Virtual.vSphere", "resourceTypeRef": { "id": "Infrastructure.Virtual", "label": "Virtual Machine" }, "name": "dev-005", "description": "Basic IaaS CentOS Machine", "status": "ACTIVE", "catalogItem": NULL, "requestId": "b3719474-a779-4351-bf45-b3b5445f1df4", "requestState": "SUCCESSFUL", "providerBinding": { "bindingId": "9f9565a1-ab52-4470-85ee-ee00f3b9e465", "providerRef": { "id": "2360c273-a3b4-4c67-b7e4-e54f2ca5c0d3", "label": "Infrastructure Service" } }, "owners": [ { "tenantName": "vsphere.local", "ref": "devmgr@corp.local", "type": "USER", "value": "Development Manager" } ], "organization": { "tenantRef": "vsphere.local", "tenantLabel": "vsphere.local", "subtenantRef": "1a2fe95f-8e39-452a-ac95-77168705b873", "subtenantLabel": "Development" }, "dateCreated": "2018-07-03T14:53:49.485Z", "lastUpdated": "2018-07-09T06:34:54.206Z", "hasLease": "true", "lease": { "start": "2018-07-03T14:47:49.539Z", "end": "2018-07-14T06:45:00.000Z" }, "leaseForDisplay": { "type": "timeSpan", "unit": "DAYS", "amount": "11" }, "hasCosts": "true", "costs": { "leaseRate": { "type": "moneyTimeRate", "cost": { "type": "money", "currencyCode": "USD", "amount": "1.3609999987152779" }, "basis": { "type": "timeSpan", "unit": "DAYS", "amount": "1" } } }, "costToDate": { "type": "money", "currencyCode": "USD", "amount": "13.60999998715278" }, "totalCost": { "type": "money", "currencyCode": "USD", "amount": "14.970999985868056" }, "expenseMonthToDate": { "amount": "10.613", "currencyCode": "USD", "asOnDate": "2018-07-13T05:01:51.603Z" }, "parentResourceRef": { "id": "823993a4-f3ef-448e-a346-79316b1863c1", "label": "CentOS Lease-58278381" }, "hasChildren": "false", "operations": [ ], "forms": { "catalogResourceInfoHidden": "true", "details": { "type": "extension", "extensionId": "csp.places.iaas.item.details", "extensionPointId": NULL } }, "resourceData": { "entries": [ { "key": "MachineGuestOperatingSystem", "value": { "type": "string", "value": "CentOS 4\/5 or later (64-bit)" } }, { "key": "MachineMemory", "value": { "type": "integer", "value": "2048" } }, { "key": "DISK_VOLUMES", "value": { "type": "multiple", "elementTypeId": "COMPLEX", "items": [ { "type": "complex", "componentTypeId": "com.vmware.csp.component.iaas.proxy.provider", "componentId": NULL, "classId": "dynamicops.api.model.DiskInputModel", "typeFilter": NULL, "values": { "entries": [ { "key": "DISK_INPUT_ID", "value": { "type": "string", "value": "DISK_INPUT_ID1" } }, { "key": "DISK_CAPACITY", "value": { "type": "integer", "value": "10" } }, { "key": "DISK_LABEL", "value": { "type": "string", "value": "Hard disk 1" } } ] } } ] } }, { "key": "MachineBlueprintName", "value": { "type": "string", "value": "CentOS Lease" } }, { "key": "MachineInterfaceType", "value": { "type": "string", "value": "vSphere" } }, { "key": "MachineCPU", "value": { "type": "integer", "value": "1" } }, { "key": "MachineExpirationDate", "value": { "type": "dateTime", "value": "2018-07-14T06:45:00.000Z" } }, { "key": "IS_COMPONENT_MACHINE", "value": { "type": "boolean", "value": "false" } }, { "key": "ChangeLease", "value": { "type": "boolean", "value": "true" } }, { "key": "endpointExternalReferenceId", "value": { "type": "string", "value": "706b710a-0f5a-46a4-802c-d07d93972e0a" } }, { "key": "MachineInterfaceDisplayName", "value": { "type": "string", "value": "vSphere (vCenter)" } }, { "key": "VirtualMachine.Admin.UUID", "value": { "type": "string", "value": "50083498-95b5-5299-a946-dd23cc6b3475" } }, { "key": "MachineReservationName", "value": { "type": "string", "value": "Development Reservation" } }, { "key": "NETWORK_LIST", "value": { "type": "multiple", "elementTypeId": "COMPLEX", "items": [ { "type": "complex", "componentTypeId": "com.vmware.csp.component.iaas.proxy.provider", "componentId": NULL, "classId": "dynamicops.api.model.NetworkViewModel", "typeFilter": NULL, "values": { "entries": [ { "key": "NETWORK_NAME", "value": { "type": "string", "value": "VM-RegionA01-vDS-COMP" } }, { "key": "NETWORK_NETWORK_NAME", "value": { "type": "string", "value": "DefaultExternalNetworkProfile" } }, { "key": "NETWORK_ADDRESS", "value": { "type": "string", "value": "192.168.110.205" } }, { "key": "NETWORK_MAC_ADDRESS", "value": { "type": "string", "value": "00:50:56:88:c7:76" } }, { "key": "NETWORK_PROFILE", "value": { "type": "string", "value": "Default External Network Profile" } } ] } } ] } }, { "key": "Component", "value": { "type": "string", "value": "CentOS" } }, { "key": "SNAPSHOT_LIST", "value": { "type": "multiple", "elementTypeId": "COMPLEX", "items": [ ] } }, { "key": "MachineStatus", "value": { "type": "string", "value": "Off" } }, { "key": "MachineType", "value": { "type": "string", "value": "Virtual" } }, { "key": "MachineStorage", "value": { "type": "integer", "value": "10" } }, { "key": "EXTERNAL_REFERENCE_ID", "value": { "type": "string", "value": "vm-464" } }, { "key": "MachineGroupName", "value": { "type": "string", "value": "Development" } }, { "key": "ip_address", "value": { "type": "string", "value": "192.168.110.205" } }, { "key": "ChangeOwner", "value": { "type": "boolean", "value": "true" } }, { "key": "machineId", "value": { "type": "string", "value": "9f9565a1-ab52-4470-85ee-ee00f3b9e465" } }, { "key": "MachineName", "value": { "type": "string", "value": "dev-005" } }, { "key": "MachineDestructionDate", "value": { "type": "dateTime", "value": "2018-07-24T06:45:00.000Z" } }, { "key": "Reconfigure", "value": { "type": "boolean", "value": "true" } }, { "key": "MachineDailyCost", "value": { "type": "decimal", "value": "0.0" } } ] }, "destroyDate": "2018-07-24T06:45:00.000Z", "pendingRequests": [ { "@type": "ResourceActionRequest", "id": "b9157af0-74d3-4985-b443-dd9f03d066ff", "iconId": "machineReconfigure.png", "version": "1", "requestNumber": "85", "state": "PENDING_PRE_APPROVAL", "description": NULL, "reasons": "", "requestedFor": "devmgr@corp.local", "requestedBy": "devmgr@corp.local", "organization": { "tenantRef": "vsphere.local", "tenantLabel": "vsphere.local", "subtenantRef": "1a2fe95f-8e39-452a-ac95-77168705b873", "subtenantLabel": "Development" }, "requestorEntitlementId": "6eff3893-bf07-41f5-b726-466896c54974", "preApprovalId": "92559ed9-49ae-47e6-b350-9b9ddc45914d", "postApprovalId": NULL, "dateCreated": "2018-07-13T11:23:13.045Z", "lastUpdated": "2018-07-13T11:23:23.807Z", "dateSubmitted": "2018-07-13T11:23:13.045Z", "dateApproved": NULL, "dateCompleted": NULL, "quote": { "leasePeriod": NULL, "leaseRate": NULL, "totalLeaseCost": NULL }, "requestCompletion": NULL, "requestData": { "entries": [ { "key": "Cafe.Shim.VirtualMachine.Reconfigure.Storages", "value": { "type": "string", "value": "[{\"ExternalId\":\"6000C29b-a176-d43c-e176-e4249f38e3c4\",\"CapacityInGB\":10,\"StoragePath\":\"RegionA01-ISCSI01-COMP01\",\"StoragePolicy\":NULL,\"StoragePolicyMode\":NULL,\"Label\":\"Hard disk 1\",\"Device\":NULL,\"CustomProperties\":[{\"PropertyName\":\"Name\",\"PropertyValue\":\"Hard disk 1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false}]}]" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.UpdatedMemorySize", "value": { "type": "integer", "value": "4096" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.PowerActionSelector", "value": { "type": "string", "value": "0" } }, { "key": "Cafe.Shim.VirtualMachine.TotalStorageSize", "value": { "type": "decimal", "value": "10.0" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.PropertyBag", "value": { "type": "string", "value": "[{\"PropertyName\":\"_number_of_instances\",\"PropertyValue\":\"1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"Cafe.Shim.VirtualMachine.TotalStorageSize\",\"PropertyValue\":\"10\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"trace_id\",\"PropertyValue\":\"XmNhaDGC\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.AgentID\",\"PropertyValue\":\"f73e0842-0b36-eca6-06c6-7b179dc32bee\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.Hostname\",\"PropertyValue\":\"RegionA01-COMP01\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.TotalDiskUsage\",\"PropertyValue\":\"10240\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.UUID\",\"PropertyValue\":\"50083498-95b5-5299-a946-dd23cc6b3475\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Component.Cluster.Index\",\"PropertyValue\":\"0\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Component.Id\",\"PropertyValue\":\"CentOS\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Component.TypeId\",\"PropertyValue\":\"Infrastructure.CatalogItem.Machine.Virtual.vSphere\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Id\",\"PropertyValue\":\"CentOSLease\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Name\",\"PropertyValue\":\"CentOS Lease\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.CPU.Count\",\"PropertyValue\":\"1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Memory.Size\",\"PropertyValue\":\"2048\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Storage.Name\",\"PropertyValue\":\"RegionA01-ISCSI01-COMP01\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"Vrm.ProxyAgent.Uri\",\"PropertyValue\":\"https:\/\/iaas-01a.corp.local\/VMPS2Proxy\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false}]" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.UpdatedCpuCount", "value": NULL }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.RequestDate", "value": { "type": "string", "value": "2018-07-13T11:22:00" } }, { "key": "machineId", "value": { "type": "string", "value": "9f9565a1-ab52-4470-85ee-ee00f3b9e465" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.Requestor", "value": { "type": "string", "value": "devmgr@corp.local" } }, { "key": "MachineName", "value": { "type": "string", "value": "dev-005" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.CpuCount", "value": { "type": "integer", "value": "1" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.MemorySize", "value": { "type": "integer", "value": "4096" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.ExecutionSelector", "value": { "type": "string", "value": "1" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.Networks", "value": { "type": "string", "value": "[{\"NetworkName\":\"VM-RegionA01-vDS-COMP\",\"MacAddress\":\"00:50:56:88:c7:76\",\"CustomProperties\":[{\"PropertyName\":\"AddressType\",\"PropertyValue\":\"Static\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"DnsSuffix\",\"PropertyValue\":\"corp.local\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"Gateway\",\"PropertyValue\":\"192.168.110.1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"NetworkName\",\"PropertyValue\":\"DefaultExternalNetworkProfile\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"NetworkProfileName\",\"PropertyValue\":\"Default External Network Profile\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"PortID\",\"PropertyValue\":\"389\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"PrimaryDns\",\"PropertyValue\":\"192.168.110.10\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"SubnetMask\",\"PropertyValue\":\"255.255.255.0\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false}]}]" } }, { "key": "operationId", "value": { "type": "string", "value": "Infrastructure.Machine.Action.Reconfigure" } }, { "key": "Cafe.Shim.VirtualMachine.Reason", "value": { "type": "string", "value": "" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.AllowForceShutdown", "value": { "type": "string", "value": "False" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.UpdatedTotalStorageSize", "value": NULL } ] }, "retriesRemaining": "3", "requestedItemName": "Reconfigure - dev-005", "requestedItemDescription": "{com.vmware.csp.component.iaas.proxy.provider@resource.action.name.desc.machine.Reconfigure}", "components": NULL, "stateName": "Pending Approval", "resourceRef": { "id": "aec4e7e3-1e7a-433a-9817-6aff478d20d9", "label": "dev-005" }, "resourceActionRef": { "id": "db5e2c7b-9f4b-4979-b605-c1060793d8ae", "label": "Reconfigure" }, "phase": "PENDING_PRE_APPROVAL", "executionStatus": "STARTED", "waitingStatus": "WAITING_FOR_APPROVAL", "approvalStatus": "PENDING" } ] } )
r = json.dumps( { "id": "aec4e7e3-1e7a-433a-9817-6aff478d20d9", "iconId": "Infrastructure.CatalogItem.Machine.Virtual.vSphere", "resourceTypeRef": { "id": "Infrastructure.Virtual", "label": "Virtual Machine" }, "name": "dev-005", "description": "Basic IaaS CentOS Machine", "status": "ACTIVE", "catalogItem": "", "requestId": "b3719474-a779-4351-bf45-b3b5445f1df4", "requestState": "SUCCESSFUL", "providerBinding": { "bindingId": "9f9565a1-ab52-4470-85ee-ee00f3b9e465", "providerRef": { "id": "2360c273-a3b4-4c67-b7e4-e54f2ca5c0d3", "label": "Infrastructure Service" } }, "owners": [ { "tenantName": "vsphere.local", "ref": "devmgr@corp.local", "type": "USER", "value": "Development Manager" } ], "organization": { "tenantRef": "vsphere.local", "tenantLabel": "vsphere.local", "subtenantRef": "1a2fe95f-8e39-452a-ac95-77168705b873", "subtenantLabel": "Development" }, "dateCreated": "2018-07-03T14:53:49.485Z", "lastUpdated": "2018-07-09T06:34:54.206Z", "hasLease": "true", "lease": { "start": "2018-07-03T14:47:49.539Z", "end": "2018-07-14T06:45:00.000Z" }, "leaseForDisplay": { "type": "timeSpan", "unit": "DAYS", "amount": "11" }, "hasCosts": "true", "costs": { "leaseRate": { "type": "moneyTimeRate", "cost": { "type": "money", "currencyCode": "USD", "amount": "1.3609999987152779" }, "basis": { "type": "timeSpan", "unit": "DAYS", "amount": "1" } } }, "costToDate": { "type": "money", "currencyCode": "USD", "amount": "13.60999998715278" }, "totalCost": { "type": "money", "currencyCode": "USD", "amount": "14.970999985868056" }, "expenseMonthToDate": { "amount": "10.613", "currencyCode": "USD", "asOnDate": "2018-07-13T05:01:51.603Z" }, "parentResourceRef": { "id": "823993a4-f3ef-448e-a346-79316b1863c1", "label": "CentOS Lease-58278381" }, "hasChildren": "false", "operations": [ ], "forms": { "catalogResourceInfoHidden": "true", "details": { "type": "extension", "extensionId": "csp.places.iaas.item.details", "extensionPointId": "" } }, "resourceData": { "entries": [ { "key": "MachineGuestOperatingSystem", "value": { "type": "string", "value": "CentOS 4\/5 or later (64-bit)" } }, { "key": "MachineMemory", "value": { "type": "integer", "value": "2048" } }, { "key": "DISK_VOLUMES", "value": { "type": "multiple", "elementTypeId": "COMPLEX", "items": [ { "type": "complex", "componentTypeId": "com.vmware.csp.component.iaas.proxy.provider", "componentId": "", "classId": "dynamicops.api.model.DiskInputModel", "typeFilter": "", "values": { "entries": [ { "key": "DISK_INPUT_ID", "value": { "type": "string", "value": "DISK_INPUT_ID1" } }, { "key": "DISK_CAPACITY", "value": { "type": "integer", "value": "10" } }, { "key": "DISK_LABEL", "value": { "type": "string", "value": "Hard disk 1" } } ] } } ] } }, { "key": "MachineBlueprintName", "value": { "type": "string", "value": "CentOS Lease" } }, { "key": "MachineInterfaceType", "value": { "type": "string", "value": "vSphere" } }, { "key": "MachineCPU", "value": { "type": "integer", "value": "1" } }, { "key": "MachineExpirationDate", "value": { "type": "dateTime", "value": "2018-07-14T06:45:00.000Z" } }, { "key": "IS_COMPONENT_MACHINE", "value": { "type": "boolean", "value": "false" } }, { "key": "ChangeLease", "value": { "type": "boolean", "value": "true" } }, { "key": "endpointExternalReferenceId", "value": { "type": "string", "value": "706b710a-0f5a-46a4-802c-d07d93972e0a" } }, { "key": "MachineInterfaceDisplayName", "value": { "type": "string", "value": "vSphere (vCenter)" } }, { "key": "VirtualMachine.Admin.UUID", "value": { "type": "string", "value": "50083498-95b5-5299-a946-dd23cc6b3475" } }, { "key": "MachineReservationName", "value": { "type": "string", "value": "Development Reservation" } }, { "key": "NETWORK_LIST", "value": { "type": "multiple", "elementTypeId": "COMPLEX", "items": [ { "type": "complex", "componentTypeId": "com.vmware.csp.component.iaas.proxy.provider", "componentId": "", "classId": "dynamicops.api.model.NetworkViewModel", "typeFilter": "", "values": { "entries": [ { "key": "NETWORK_NAME", "value": { "type": "string", "value": "VM-RegionA01-vDS-COMP" } }, { "key": "NETWORK_NETWORK_NAME", "value": { "type": "string", "value": "DefaultExternalNetworkProfile" } }, { "key": "NETWORK_ADDRESS", "value": { "type": "string", "value": "192.168.110.205" } }, { "key": "NETWORK_MAC_ADDRESS", "value": { "type": "string", "value": "00:50:56:88:c7:76" } }, { "key": "NETWORK_PROFILE", "value": { "type": "string", "value": "Default External Network Profile" } } ] } } ] } }, { "key": "Component", "value": { "type": "string", "value": "CentOS" } }, { "key": "SNAPSHOT_LIST", "value": { "type": "multiple", "elementTypeId": "COMPLEX", "items": [ ] } }, { "key": "MachineStatus", "value": { "type": "string", "value": "Off" } }, { "key": "MachineType", "value": { "type": "string", "value": "Virtual" } }, { "key": "MachineStorage", "value": { "type": "integer", "value": "10" } }, { "key": "EXTERNAL_REFERENCE_ID", "value": { "type": "string", "value": "vm-464" } }, { "key": "MachineGroupName", "value": { "type": "string", "value": "Development" } }, { "key": "ip_address", "value": { "type": "string", "value": "192.168.110.205" } }, { "key": "ChangeOwner", "value": { "type": "boolean", "value": "true" } }, { "key": "machineId", "value": { "type": "string", "value": "9f9565a1-ab52-4470-85ee-ee00f3b9e465" } }, { "key": "MachineName", "value": { "type": "string", "value": "dev-005" } }, { "key": "MachineDestructionDate", "value": { "type": "dateTime", "value": "2018-07-24T06:45:00.000Z" } }, { "key": "Reconfigure", "value": { "type": "boolean", "value": "true" } }, { "key": "MachineDailyCost", "value": { "type": "decimal", "value": "0.0" } } ] }, "destroyDate": "2018-07-24T06:45:00.000Z", "pendingRequests": [ { "@type": "ResourceActionRequest", "id": "b9157af0-74d3-4985-b443-dd9f03d066ff", "iconId": "machineReconfigure.png", "version": "1", "requestNumber": "85", "state": "PENDING_PRE_APPROVAL", "description": "", "reasons": "", "requestedFor": "devmgr@corp.local", "requestedBy": "devmgr@corp.local", "organization": { "tenantRef": "vsphere.local", "tenantLabel": "vsphere.local", "subtenantRef": "1a2fe95f-8e39-452a-ac95-77168705b873", "subtenantLabel": "Development" }, "requestorEntitlementId": "6eff3893-bf07-41f5-b726-466896c54974", "preApprovalId": "92559ed9-49ae-47e6-b350-9b9ddc45914d", "postApprovalId": "", "dateCreated": "2018-07-13T11:23:13.045Z", "lastUpdated": "2018-07-13T11:23:23.807Z", "dateSubmitted": "2018-07-13T11:23:13.045Z", "dateApproved": "", "dateCompleted": "", "quote": { "leasePeriod": "", "leaseRate": "", "totalLeaseCost": "" }, "requestCompletion": "", "requestData": { "entries": [ { "key": "Cafe.Shim.VirtualMachine.Reconfigure.Storages", "value": { "type": "string", "value": "[{\"ExternalId\":\"6000C29b-a176-d43c-e176-e4249f38e3c4\",\"CapacityInGB\":10,\"StoragePath\":\"RegionA01-ISCSI01-COMP01\",\"StoragePolicy\":"",\"StoragePolicyMode\":"",\"Label\":\"Hard disk 1\",\"Device\":"",\"CustomProperties\":[{\"PropertyName\":\"Name\",\"PropertyValue\":\"Hard disk 1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false}]}]" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.UpdatedMemorySize", "value": { "type": "integer", "value": "4096" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.PowerActionSelector", "value": { "type": "string", "value": "0" } }, { "key": "Cafe.Shim.VirtualMachine.TotalStorageSize", "value": { "type": "decimal", "value": "10.0" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.PropertyBag", "value": { "type": "string", "value": "[{\"PropertyName\":\"_number_of_instances\",\"PropertyValue\":\"1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"Cafe.Shim.VirtualMachine.TotalStorageSize\",\"PropertyValue\":\"10\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"trace_id\",\"PropertyValue\":\"XmNhaDGC\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.AgentID\",\"PropertyValue\":\"f73e0842-0b36-eca6-06c6-7b179dc32bee\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.Hostname\",\"PropertyValue\":\"RegionA01-COMP01\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.TotalDiskUsage\",\"PropertyValue\":\"10240\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Admin.UUID\",\"PropertyValue\":\"50083498-95b5-5299-a946-dd23cc6b3475\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Component.Cluster.Index\",\"PropertyValue\":\"0\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Component.Id\",\"PropertyValue\":\"CentOS\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Component.TypeId\",\"PropertyValue\":\"Infrastructure.CatalogItem.Machine.Virtual.vSphere\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Id\",\"PropertyValue\":\"CentOSLease\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Cafe.Blueprint.Name\",\"PropertyValue\":\"CentOS Lease\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.CPU.Count\",\"PropertyValue\":\"1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Memory.Size\",\"PropertyValue\":\"2048\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"VirtualMachine.Storage.Name\",\"PropertyValue\":\"RegionA01-ISCSI01-COMP01\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"Vrm.ProxyAgent.Uri\",\"PropertyValue\":\"https:\/\/iaas-01a.corp.local\/VMPS2Proxy\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false}]" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.UpdatedCpuCount", "value": "" }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.RequestDate", "value": { "type": "string", "value": "2018-07-13T11:22:00" } }, { "key": "machineId", "value": { "type": "string", "value": "9f9565a1-ab52-4470-85ee-ee00f3b9e465" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.Requestor", "value": { "type": "string", "value": "devmgr@corp.local" } }, { "key": "MachineName", "value": { "type": "string", "value": "dev-005" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.CpuCount", "value": { "type": "integer", "value": "1" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.MemorySize", "value": { "type": "integer", "value": "4096" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.ExecutionSelector", "value": { "type": "string", "value": "1" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.Networks", "value": { "type": "string", "value": "[{\"NetworkName\":\"VM-RegionA01-vDS-COMP\",\"MacAddress\":\"00:50:56:88:c7:76\",\"CustomProperties\":[{\"PropertyName\":\"AddressType\",\"PropertyValue\":\"Static\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"DnsSuffix\",\"PropertyValue\":\"corp.local\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"Gateway\",\"PropertyValue\":\"192.168.110.1\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"NetworkName\",\"PropertyValue\":\"DefaultExternalNetworkProfile\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"NetworkProfileName\",\"PropertyValue\":\"Default External Network Profile\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"PortID\",\"PropertyValue\":\"389\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"PrimaryDns\",\"PropertyValue\":\"192.168.110.10\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false},{\"PropertyName\":\"SubnetMask\",\"PropertyValue\":\"255.255.255.0\",\"IsHidden\":false,\"IsRuntime\":false,\"IsEncrypted\":false}]}]" } }, { "key": "operationId", "value": { "type": "string", "value": "Infrastructure.Machine.Action.Reconfigure" } }, { "key": "Cafe.Shim.VirtualMachine.Reason", "value": { "type": "string", "value": "" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.AllowForceShutdown", "value": { "type": "string", "value": "False" } }, { "key": "Cafe.Shim.VirtualMachine.Reconfigure.UpdatedTotalStorageSize", "value": "" } ] }, "retriesRemaining": "3", "requestedItemName": "Reconfigure - dev-005", "requestedItemDescription": "{com.vmware.csp.component.iaas.proxy.provider@resource.action.name.desc.machine.Reconfigure}", "components": "", "stateName": "Pending Approval", "resourceRef": { "id": "aec4e7e3-1e7a-433a-9817-6aff478d20d9", "label": "dev-005" }, "resourceActionRef": { "id": "db5e2c7b-9f4b-4979-b605-c1060793d8ae", "label": "Reconfigure" }, "phase": "PENDING_PRE_APPROVAL", "executionStatus": "STARTED", "waitingStatus": "WAITING_FOR_APPROVAL", "approvalStatus": "PENDING" } ] } )


res = json.loads(r)

print "Daily Lease Cost", res['costs']['leaseRate']['cost']['amount']
print "Cost To Date", res['costToDate']['amount']
print "Total Cost", res['totalCost']['amount']
print "Expense month to date", res['expenseMonthToDate']['amount']
print "  as on", res['expenseMonthToDate']['asOnDate']

for i in res['resourceData']['entries']:
	print i["key"], i["value"]
	if (i["value"].contains("value")) :
		print i["value"]["value"]
