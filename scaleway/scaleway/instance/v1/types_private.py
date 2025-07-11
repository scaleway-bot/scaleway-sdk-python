# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
)
from scaleway_core.utils import (
    StrEnumMeta,
)

from .types import (
    Arch,
    AttachServerVolumeRequestVolumeType,
    BootType,
    ImageState,
    IpState,
    IpType,
    ListServersRequestOrder,
    PlacementGroupPolicyMode,
    PlacementGroupPolicyType,
    PrivateNICState,
    SecurityGroupPolicy,
    SecurityGroupRuleAction,
    SecurityGroupRuleDirection,
    SecurityGroupRuleProtocol,
    SecurityGroupState,
    ServerAction,
    ServerFilesystemState,
    ServerIpIpFamily,
    ServerIpProvisioningMode,
    ServerIpState,
    ServerState,
    ServerTypesAvailability,
    SnapshotState,
    SnapshotVolumeType,
    TaskStatus,
    VolumeServerState,
    VolumeServerVolumeType,
    VolumeState,
    VolumeVolumeType,ServerSummary,Bootscript,Volume,VolumeSummary,ServerTypeNetworkInterface,ServerTypeVolumeConstraintSizes,Image,PlacementGroup,PrivateNIC,SecurityGroupSummary,ServerFilesystem,ServerIp,ServerIpv6,ServerLocation,ServerMaintenance,VolumeServer,SnapshotBaseVolume,ServerTypeCapabilities,ServerTypeGPUInfo,ServerTypeNetwork,ServerTypeVolumeConstraintsByType,VolumeTypeCapabilities,VolumeTypeConstraints,Server,VolumeTemplate,Ip,SecurityGroup,SecurityGroupRule,VolumeServerTemplate,Snapshot,Task,Dashboard,PlacementGroupServer,GetServerTypesAvailabilityResponseAvailability,ServerType,VolumeType,ServerActionRequestVolumeBackupTemplate,SetSecurityGroupRulesRequestRule,VolumeImageUpdateTemplate,SecurityGroupTemplate,ApplyBlockMigrationRequest,AttachServerFileSystemRequest,AttachServerFileSystemResponse,AttachServerVolumeRequest,AttachServerVolumeResponse,CheckBlockMigrationOrganizationQuotasRequest,CreateImageRequest,CreateImageResponse,CreateIpRequest,CreateIpResponse,CreatePlacementGroupRequest,CreatePlacementGroupResponse,CreatePrivateNICRequest,CreatePrivateNICResponse,CreateSecurityGroupRequest,CreateSecurityGroupResponse,CreateSecurityGroupRuleRequest,CreateSecurityGroupRuleResponse,CreateServerRequest,CreateServerResponse,CreateSnapshotRequest,CreateSnapshotResponse,CreateVolumeRequest,CreateVolumeResponse,DeleteImageRequest,DeleteIpRequest,DeletePlacementGroupRequest,DeletePrivateNICRequest,DeleteSecurityGroupRequest,DeleteSecurityGroupRuleRequest,DeleteServerRequest,DeleteServerUserDataRequest,DeleteSnapshotRequest,DeleteVolumeRequest,DetachServerFileSystemRequest,DetachServerFileSystemResponse,DetachServerVolumeRequest,DetachServerVolumeResponse,ExportSnapshotRequest,ExportSnapshotResponse,GetDashboardRequest,GetDashboardResponse,GetImageRequest,GetImageResponse,GetIpRequest,GetIpResponse,GetPlacementGroupRequest,GetPlacementGroupResponse,GetPlacementGroupServersRequest,GetPlacementGroupServersResponse,GetPrivateNICRequest,GetPrivateNICResponse,GetSecurityGroupRequest,GetSecurityGroupResponse,GetSecurityGroupRuleRequest,GetSecurityGroupRuleResponse,GetServerCompatibleTypesRequest,GetServerRequest,GetServerResponse,GetServerTypesAvailabilityRequest,GetServerTypesAvailabilityResponse,GetSnapshotRequest,GetSnapshotResponse,GetVolumeRequest,GetVolumeResponse,ListDefaultSecurityGroupRulesRequest,ListImagesRequest,ListImagesResponse,ListIpsRequest,ListIpsResponse,ListPlacementGroupsRequest,ListPlacementGroupsResponse,ListPrivateNICsRequest,ListPrivateNICsResponse,ListSecurityGroupRulesRequest,ListSecurityGroupRulesResponse,ListSecurityGroupsRequest,ListSecurityGroupsResponse,ListServerActionsRequest,ListServerActionsResponse,ListServerUserDataRequest,ListServerUserDataResponse,ListServersRequest,ListServersResponse,ListServersTypesRequest,ListServersTypesResponse,ListSnapshotsRequest,ListSnapshotsResponse,ListVolumesRequest,ListVolumesResponse,ListVolumesTypesRequest,ListVolumesTypesResponse,MigrationPlan,PlanBlockMigrationRequest,ServerActionRequest,ServerActionResponse,ServerCompatibleTypes,SetImageRequest,SetPlacementGroupRequest,SetPlacementGroupResponse,SetPlacementGroupServersRequest,SetPlacementGroupServersResponse,SetSecurityGroupRulesRequest,SetSecurityGroupRulesResponse,UpdateImageRequest,UpdateImageResponse,UpdateIpRequest,UpdateIpResponse,UpdatePlacementGroupRequest,UpdatePlacementGroupResponse,UpdatePlacementGroupServersRequest,UpdatePlacementGroupServersResponse,UpdatePrivateNICRequest,UpdateSecurityGroupRequest,UpdateSecurityGroupResponse,UpdateSecurityGroupRuleRequest,UpdateSecurityGroupRuleResponse,UpdateServerRequest,UpdateServerResponse,UpdateSnapshotRequest,UpdateSnapshotResponse,UpdateVolumeRequest,UpdateVolumeResponse,)

@dataclass
class _SetImageResponse:
    image: Optional[Image]

@dataclass
class _SetSecurityGroupRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    id: str
    """
    UUID of the security group.
    """
    name: str
    """
    Name of the security group.
    """
    description: str
    """
    Description of the security group.
    """
    enable_default_security: bool
    """
    True to block SMTP on IPv4 and IPv6. This feature is read only, please open a support ticket if you need to make it configurable.
    """
    tags: Optional[List[str]]
    """
    Tags of the security group.
    """
    creation_date: Optional[datetime]
    """
    Creation date of the security group (will be ignored).
    """
    modification_date: Optional[datetime]
    """
    Modification date of the security group (will be ignored).
    """
    project_default: bool
    """
    True use this security group for future Instances created in this project.
    """
    stateful: bool
    """
    True to set the security group as stateful.
    """
    inbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default inbound policy.
    """
    outbound_default_policy: Optional[SecurityGroupPolicy]
    """
    Default outbound policy.
    """
    organization: Optional[str]
    """
    Security groups Organization ID.
    """
    project: Optional[str]
    """
    Security group Project ID.
    """
    organization_default: Optional[bool]
    """
    Please use project_default instead.
    """
    servers: Optional[List[ServerSummary]]
    """
    Instances attached to this security group.
    """

@dataclass
class _SetSecurityGroupResponse:
    security_group: Optional[SecurityGroup]

@dataclass
class _SetSecurityGroupRuleRequest:
    security_group_id: str
    security_group_rule_id: str
    id: str
    ip_range: str
    position: int
    editable: bool
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    protocol: Optional[SecurityGroupRuleProtocol]
    direction: Optional[SecurityGroupRuleDirection]
    action: Optional[SecurityGroupRuleAction]
    dest_port_from: Optional[int]
    dest_port_to: Optional[int]

@dataclass
class _SetSecurityGroupRuleResponse:
    rule: Optional[SecurityGroupRule]

@dataclass
class _SetServerRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    id: str
    """
    Instance unique ID.
    """
    name: str
    """
    Instance name.
    """
    commercial_type: str
    """
    Instance commercial type (eg. GP1-M).
    """
    organization: Optional[str]
    """
    Instance Organization ID.
    """
    dynamic_ip_required: bool
    """
    True if a dynamic IPv4 is required.
    """
    hostname: str
    """
    Instance host name.
    """
    protected: bool
    """
    Instance protection option is activated.
    """
    state_detail: str
    """
    Instance state_detail.
    """
    project: Optional[str]
    """
    Instance Project ID.
    """
    allowed_actions: Optional[List[ServerAction]]
    """
    Provide a list of allowed actions on the server.
    """
    tags: Optional[List[str]]
    """
    Tags associated with the Instance.
    """
    creation_date: Optional[datetime]
    """
    Instance creation date.
    """
    routed_ip_enabled: Optional[bool]
    """
    True to configure the instance so it uses the new routed IP mode (once this is set to True you cannot set it back to False).
    """
    enable_ipv6: Optional[bool]
    """
    True if IPv6 is enabled (deprecated and always `False` when `routed_ip_enabled` is `True`).
    """
    image: Optional[Image]
    """
    Provide information on the Instance image.
    """
    private_ip: Optional[str]
    """
    Instance private IP address (deprecated and always `null` when `routed_ip_enabled` is `True`).
    """
    public_ip: Optional[ServerIp]
    """
    Information about the public IP (deprecated in favor of `public_ips`).
    """
    public_ips: Optional[List[ServerIp]]
    """
    Information about all the public IPs attached to the server.
    """
    modification_date: Optional[datetime]
    """
    Instance modification date.
    """
    state: Optional[ServerState]
    """
    Instance state.
    """
    location: Optional[ServerLocation]
    """
    Instance location.
    """
    ipv6: Optional[ServerIpv6]
    """
    Instance IPv6 address (deprecated when `routed_ip_enabled` is `True`).
    """
    boot_type: Optional[BootType]
    """
    Instance boot type.
    """
    volumes: Optional[Dict[str, Volume]]
    """
    Instance volumes.
    """
    security_group: Optional[SecurityGroupSummary]
    """
    Instance security group.
    """
    maintenances: Optional[List[ServerMaintenance]]
    """
    Instance planned maintenances.
    """
    arch: Optional[Arch]
    """
    Instance architecture (refers to the CPU architecture used for the Instance, e.g. x86_64, arm64).
    """
    placement_group: Optional[PlacementGroup]
    """
    Instance placement group.
    """
    private_nics: Optional[List[PrivateNIC]]
    """
    Instance private NICs.
    """
    admin_password_encryption_ssh_key_id: Optional[str]
    """
    The public_key value of this key is used to encrypt the admin password. When set to an empty string, reset this value and admin_password_encrypted_value to an empty string so a new password may be generated.
    """

@dataclass
class _SetServerResponse:
    server: Optional[Server]

@dataclass
class _SetSnapshotRequest:
    id: str
    name: str
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    organization: Optional[str]
    volume_type: Optional[VolumeVolumeType]
    size: int
    state: Optional[SnapshotState]
    base_volume: Optional[SnapshotBaseVolume]
    creation_date: Optional[datetime]
    modification_date: Optional[datetime]
    project: Optional[str]
    snapshot_id: str
    tags: Optional[List[str]]

@dataclass
class _SetSnapshotResponse:
    snapshot: Optional[Snapshot]
