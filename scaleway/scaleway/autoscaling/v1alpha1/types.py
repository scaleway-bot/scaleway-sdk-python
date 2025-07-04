# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
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

class InstanceGroupEventLevel(str, Enum, metaclass=StrEnumMeta):
    INFO = "info"
    SUCCESS = "success"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)

class InstanceGroupEventSource(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_SOURCE = "unknown_source"
    WATCHER = "watcher"
    SCALER = "scaler"
    INSTANCE_MANAGER = "instance_manager"
    SUPERVISOR = "supervisor"

    def __str__(self) -> str:
        return str(self.value)

class InstancePolicyAction(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_ACTION = "unknown_action"
    SCALE_UP = "scale_up"
    SCALE_DOWN = "scale_down"

    def __str__(self) -> str:
        return str(self.value)

class InstancePolicyType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_TYPE = "unknown_type"
    FLAT_COUNT = "flat_count"
    PERCENT_OF_TOTAL_GROUP = "percent_of_total_group"
    SET_TOTAL_GROUP = "set_total_group"

    def __str__(self) -> str:
        return str(self.value)

class InstanceTemplateStatus(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)

class ListInstanceGroupEventsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)

class ListInstanceGroupsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)

class ListInstancePoliciesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)

class ListInstanceTemplatesRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_DESC = "created_at_desc"
    CREATED_AT_ASC = "created_at_asc"

    def __str__(self) -> str:
        return str(self.value)

class MetricAggregate(str, Enum, metaclass=StrEnumMeta):
    AGGREGATE_UNKNOWN = "aggregate_unknown"
    AGGREGATE_AVERAGE = "aggregate_average"
    AGGREGATE_MAX = "aggregate_max"
    AGGREGATE_MIN = "aggregate_min"
    AGGREGATE_SUM = "aggregate_sum"

    def __str__(self) -> str:
        return str(self.value)

class MetricManagedMetric(str, Enum, metaclass=StrEnumMeta):
    MANAGED_METRIC_UNKNOWN = "managed_metric_unknown"
    MANAGED_METRIC_INSTANCE_CPU = "managed_metric_instance_cpu"
    MANAGED_METRIC_INSTANCE_NETWORK_IN = "managed_metric_instance_network_in"
    MANAGED_METRIC_INSTANCE_NETWORK_OUT = "managed_metric_instance_network_out"
    MANAGED_LOADBALANCER_BACKEND_CONNECTIONS_RATE = "managed_loadbalancer_backend_connections_rate"
    MANAGED_LOADBALANCER_BACKEND_THROUGHPUT = "managed_loadbalancer_backend_throughput"

    def __str__(self) -> str:
        return str(self.value)

class MetricOperator(str, Enum, metaclass=StrEnumMeta):
    OPERATOR_UNKNOWN = "operator_unknown"
    OPERATOR_GREATER_THAN = "operator_greater_than"
    OPERATOR_LESS_THAN = "operator_less_than"

    def __str__(self) -> str:
        return str(self.value)

class UpdateInstancePolicyRequestMetricAggregate(str, Enum, metaclass=StrEnumMeta):
    AGGREGATE_UNKNOWN = "aggregate_unknown"
    AGGREGATE_AVERAGE = "aggregate_average"
    AGGREGATE_MAX = "aggregate_max"
    AGGREGATE_MIN = "aggregate_min"
    AGGREGATE_SUM = "aggregate_sum"

    def __str__(self) -> str:
        return str(self.value)

class UpdateInstancePolicyRequestMetricManagedMetric(str, Enum, metaclass=StrEnumMeta):
    MANAGED_METRIC_UNKNOWN = "managed_metric_unknown"
    MANAGED_METRIC_INSTANCE_CPU = "managed_metric_instance_cpu"
    MANAGED_METRIC_INSTANCE_NETWORK_IN = "managed_metric_instance_network_in"
    MANAGED_METRIC_INSTANCE_NETWORK_OUT = "managed_metric_instance_network_out"
    MANAGED_LOADBALANCER_BACKEND_CONNECTIONS_RATE = "managed_loadbalancer_backend_connections_rate"
    MANAGED_LOADBALANCER_BACKEND_THROUGHPUT = "managed_loadbalancer_backend_throughput"

    def __str__(self) -> str:
        return str(self.value)

class UpdateInstancePolicyRequestMetricOperator(str, Enum, metaclass=StrEnumMeta):
    OPERATOR_UNKNOWN = "operator_unknown"
    OPERATOR_GREATER_THAN = "operator_greater_than"
    OPERATOR_LESS_THAN = "operator_less_than"

    def __str__(self) -> str:
        return str(self.value)

class VolumeInstanceTemplateVolumeType(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_VOLUME_TYPE = "unknown_volume_type"
    L_SSD = "l_ssd"
    SBS = "sbs"

    def __str__(self) -> str:
        return str(self.value)

@dataclass
class VolumeInstanceTemplateFromEmpty:
    size: int
    

@dataclass
class VolumeInstanceTemplateFromSnapshot:
    snapshot_id: str
    
    size: Optional[int]
    

@dataclass
class Capacity:
    max_replicas: int
    """
    Maximum count of Instances for the Instance group.
    """
    
    min_replicas: int
    """
    Minimum count of Instances for the Instance group.
    """
    
    cooldown_delay: Optional[str]
    """
    Time (in seconds) after a scaling action during which requests to carry out a new scaling action will be denied.
    """
    

@dataclass
class Loadbalancer:
    id: str
    """
    Load Balancer ID.
    """
    
    backend_ids: List[str]
    """
    Load Balancer backend IDs.
    """
    
    private_network_id: str
    """
    ID of the Private Network attached to the Load Balancer.
    """
    

@dataclass
class Metric:
    name: str
    """
    Name or description of the metric policy.
    """
    
    operator: MetricOperator
    """
    Operator used when comparing the threshold value of the chosen `metric` to the actual sampled and aggregated value.
    """
    
    aggregate: MetricAggregate
    """
    How the values sampled for the `metric` should be aggregated.
    """
    
    sampling_range_min: int
    """
    Interval of time, in minutes, during which metric is sampled.
    """
    
    threshold: float
    """
    Threshold value to measure the aggregated sampled `metric` value against. Combined with the `operator` field, determines whether a scaling action should be triggered.
    """
    
    managed_metric: Optional[MetricManagedMetric]
    
    cockpit_metric_name: Optional[str]
    

@dataclass
class VolumeInstanceTemplate:
    name: str
    """
    Name of the volume.
    """
    
    tags: List[str]
    """
    List of tags assigned to the volume.
    """
    
    boot: bool
    """
    Force the Instance to boot on this volume.
    """
    
    volume_type: VolumeInstanceTemplateVolumeType
    """
    Type of the volume.
    """
    
    from_empty: Optional[VolumeInstanceTemplateFromEmpty]
    
    from_snapshot: Optional[VolumeInstanceTemplateFromSnapshot]
    
    perf_iops: Optional[int]
    

@dataclass
class InstanceGroupEvent:
    id: str
    """
    Instance group event ID.
    """
    
    source: InstanceGroupEventSource
    """
    Log source.
    """
    
    level: InstanceGroupEventLevel
    """
    The severity of the log.
    """
    
    name: str
    """
    Log title.
    """
    
    created_at: Optional[datetime]
    """
    Date and time of the log.
    """
    
    details: Optional[str]
    """
    Full text of the log.
    """
    

@dataclass
class InstanceGroup:
    id: str
    """
    Instance group ID.
    """
    
    project_id: str
    """
    Project ID of the Instance group.
    """
    
    name: str
    """
    Name of the Instance group.
    """
    
    tags: List[str]
    """
    Instance group tags.
    """
    
    instance_template_id: str
    """
    Template ID (ID of the Instance template to attach to the Instance group).
    """
    
    capacity: Capacity
    """
    Specification of the minimum and maximum replicas for the Instance group, and the cooldown interval between two scaling events.
    """
    
    loadbalancer: Loadbalancer
    """
    Specification of the Load Balancer linked to the Instance group.
    """
    
    error_messages: List[str]
    """
    Any configuration errors for dependencies (Load Balancer, Private Network, Instance template etc.).
    """
    
    created_at: Optional[datetime]
    """
    Date on which the Instance group was created.
    """
    
    updated_at: Optional[datetime]
    """
    Date on which the Instance group was last updated.
    """
    

@dataclass
class InstancePolicy:
    id: str
    """
    Scaling policy ID.
    """
    
    name: str
    """
    Name of scaling policy.
    """
    
    action: InstancePolicyAction
    """
    Action to execute when the metric-based condition is met.
    """
    
    type_: InstancePolicyType
    """
    How to use the number defined in `value` when determining by how many Instances to scale up/down.
    """
    
    value: int
    """
    Number representing the magnitude of the scaling action to take for the Instance group.
    """
    
    priority: int
    """
    Priority of this policy compared to all other scaling policies. The lower the number, the higher the priority (higher priority will be processed sooner in the order).
    """
    
    instance_group_id: str
    """
    Instance group ID related to this policy.
    """
    
    metric: Optional[Metric]
    

@dataclass
class InstanceTemplate:
    id: str
    """
    ID of Instance template resource.
    """
    
    commercial_type: str
    """
    Name of Instance commercial type.
    """
    
    volumes: Dict[str, VolumeInstanceTemplate]
    """
    Template of Instance volume.
    """
    
    tags: List[str]
    """
    List of tags for the Instance template.
    """
    
    project_id: str
    """
    ID of the Project containing the Instance template resource.
    """
    
    name: str
    """
    Name of Instance template.
    """
    
    private_network_ids: List[str]
    """
    Private Network IDs to attach to the new Instance.
    """
    
    image_id: Optional[str]
    """
    Instance image ID. Can be an ID of a marketplace or personal image. This image must be compatible with `volume` and `commercial_type` template.
    """
    
    security_group_id: Optional[str]
    """
    Instance security group ID (optional).
    """
    
    placement_group_id: Optional[str]
    """
    Instance placement group ID. This is optional, but it is highly recommended to set a preference for Instance location within Availability Zone.
    """
    
    public_ips_v4_count: Optional[int]
    """
    Number of flexible IPv4 addresses to attach to the new Instance.
    """
    
    public_ips_v6_count: Optional[int]
    """
    Number of flexible IPv6 addresses to attach to the new Instance.
    """
    
    status: InstanceTemplateStatus
    """
    Status of Instance template.
    """
    
    cloud_init: Optional[str]
    """
    Cloud-config file must be passed in Base64 format. Cloud-config files are special scripts designed to be run by the cloud-init process. These are generally used for initial configuration on the very first boot of a server.
    """
    
    created_at: Optional[datetime]
    """
    Date on which the Instance template was created.
    """
    
    updated_at: Optional[datetime]
    """
    Date on which the Instance template was last updated.
    """
    

@dataclass
class UpdateInstanceGroupRequestCapacity:
    max_replicas: Optional[int]
    """
    Maximum count of Instances for the Instance group.
    """
    
    min_replicas: Optional[int]
    """
    Minimum count of Instances for the Instance group.
    """
    
    cooldown_delay: Optional[str]
    """
    Time (in seconds) after a scaling action during which requests to carry out a new scaling action will be denied.
    """
    

@dataclass
class UpdateInstanceGroupRequestLoadbalancer:
    backend_ids: Optional[List[str]]
    """
    Load Balancer backend IDs.
    """
    

@dataclass
class UpdateInstancePolicyRequestMetric:
    operator: UpdateInstancePolicyRequestMetricOperator
    """
    Operator used when comparing the threshold value of the chosen `metric` to the actual sampled and aggregated value.
    """
    
    aggregate: UpdateInstancePolicyRequestMetricAggregate
    """
    How the values sampled for the `metric` should be aggregated.
    """
    
    name: Optional[str]
    """
    Name or description of your metric policy.
    """
    
    sampling_range_min: Optional[int]
    """
    Interval of time, in minutes, during which metric is sampled.
    """
    
    threshold: Optional[float]
    """
    Threshold value to measure the aggregated sampled `metric` value against. Combined with the `operator` field, determines whether a scaling action should be triggered.
    """
    
    managed_metric: Optional[UpdateInstancePolicyRequestMetricManagedMetric]
    
    cockpit_metric_name: Optional[str]
    

@dataclass
class CreateInstanceGroupRequest:
    name: str
    """
    Name of Instance group.
    """
    
    template_id: str
    """
    Template ID (ID of the Instance template to attach to the Instance group).
    """
    
    capacity: Capacity
    """
    Specification of the minimum and maximum replicas for the Instance group, and the cooldown interval between two scaling events.
    """
    
    loadbalancer: Loadbalancer
    """
    Specification of the Load Balancer to link to the Instance group.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    project_id: Optional[str]
    """
    Project ID to filter for, only Instance groups from this Project will be returned.
    """
    
    tags: Optional[List[str]]
    """
    List of tags for the Instance group.
    """
    

@dataclass
class CreateInstancePolicyRequest:
    name: str
    """
    Name of the policy.
    """
    
    action: InstancePolicyAction
    """
    Action to execute when the metric-based condition is met.
    """
    
    type_: InstancePolicyType
    """
    How to use the number defined in `value` when determining by how many Instances to scale up/down.
    """
    
    value: int
    """
    Value representing the magnitude of the scaling action to take for the Instance group. Depending on the `type` parameter, this number could represent a total number of Instances in the group, a number of Instances to add, or a percentage to scale the group by.
    """
    
    priority: int
    """
    Priority of this policy compared to all other scaling policies. This determines the processing order. The lower the number, the higher the priority.
    """
    
    instance_group_id: str
    """
    Instance group ID related to this policy.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    metric: Optional[Metric]
    

@dataclass
class CreateInstanceTemplateRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    commercial_type: str
    """
    Name of Instance commercial type.
    """
    
    volumes: Dict[str, VolumeInstanceTemplate]
    """
    Template of Instance volume.
    """
    
    image_id: Optional[str]
    """
    Instance image ID. Can be an ID of a marketplace or personal image. This image must be compatible with `volume` and `commercial_type` template.
    """
    
    tags: Optional[List[str]]
    """
    List of tags for the Instance template.
    """
    
    security_group_id: Optional[str]
    """
    Instance security group ID (optional).
    """
    
    name: str
    """
    Name of Instance template.
    """
    
    placement_group_id: Optional[str]
    """
    Instance placement group ID. This is optional, but it is highly recommended to set a preference for Instance location within Availability Zone.
    """
    
    public_ips_v4_count: Optional[int]
    """
    Number of flexible IPv4 addresses to attach to the new Instance.
    """
    
    public_ips_v6_count: Optional[int]
    """
    Number of flexible IPv6 addresses to attach to the new Instance.
    """
    
    project_id: Optional[str]
    """
    ID of the Project containing the Instance template resource.
    """
    
    private_network_ids: Optional[List[str]]
    """
    Private Network IDs to attach to the new Instance.
    """
    
    cloud_init: Optional[str]
    """
    Cloud-config file must be passed in Base64 format. Cloud-config files are special scripts designed to be run by the cloud-init process. These are generally used for initial configuration on the very first boot of a server.
    """
    

@dataclass
class DeleteInstanceGroupRequest:
    instance_group_id: str
    """
    ID of the Instance group to delete.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    

@dataclass
class DeleteInstancePolicyRequest:
    policy_id: str
    """
    ID of the policy to delete.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    

@dataclass
class DeleteInstanceTemplateRequest:
    template_id: str
    """
    ID of the template to delete.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    

@dataclass
class GetInstanceGroupRequest:
    instance_group_id: str
    """
    ID of the requested Instance group.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    

@dataclass
class GetInstancePolicyRequest:
    policy_id: str
    """
    Policy ID.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    

@dataclass
class GetInstanceTemplateRequest:
    template_id: str
    """
    Template ID of the resource.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    

@dataclass
class ListInstanceGroupEventsRequest:
    instance_group_id: str
    """
    List all event logs for the Instance group ID.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    order_by: Optional[ListInstanceGroupEventsRequestOrderBy]
    """
    Sort order of Instance groups in the response.
    """
    
    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """
    
    page_size: Optional[int]
    """
    Number of Instance groups to return per page.
    """
    

@dataclass
class ListInstanceGroupEventsResponse:
    instance_events: List[InstanceGroupEvent]
    """
    Paginated list of Instance groups.
    """
    
    total_count: int
    """
    Count of all Instance groups matching the requested criteria.
    """
    

@dataclass
class ListInstanceGroupsRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    order_by: Optional[ListInstanceGroupsRequestOrderBy]
    """
    Sort order of Instance groups in the response.
    """
    
    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """
    
    page_size: Optional[int]
    """
    Number of Instance groups to return per page.
    """
    

@dataclass
class ListInstanceGroupsResponse:
    instance_groups: List[InstanceGroup]
    """
    Paginated list of Instance groups.
    """
    
    total_count: int
    """
    Count of all Instance groups matching the requested criteria.
    """
    

@dataclass
class ListInstancePoliciesRequest:
    instance_group_id: str
    """
    Instance group ID.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    order_by: Optional[ListInstancePoliciesRequestOrderBy]
    """
    Sort order of Instance groups in the response.
    """
    
    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """
    
    page_size: Optional[int]
    """
    Number of scaling policies to return per page.
    """
    

@dataclass
class ListInstancePoliciesResponse:
    policies: List[InstancePolicy]
    """
    Paginated list of policies.
    """
    
    total_count: int
    """
    Count of all policies matching the requested criteria.
    """
    

@dataclass
class ListInstanceTemplatesRequest:
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    order_by: Optional[ListInstanceTemplatesRequestOrderBy]
    """
    Sort order of Instance groups in the response.
    """
    
    page: Optional[int]
    """
    Page number to return, from the paginated results.
    """
    
    page_size: Optional[int]
    """
    Number of Instance groups to return per page.
    """
    

@dataclass
class ListInstanceTemplatesResponse:
    total_count: int
    """
    Count of all templates matching the requested criteria.
    """
    
    instance_templates: List[InstanceTemplate]
    """
    Paginated list of Instance templates.
    """
    

@dataclass
class UpdateInstanceGroupRequest:
    instance_group_id: str
    """
    Instance group ID to update.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    name: Optional[str]
    """
    Name of Instance group.
    """
    
    tags: Optional[List[str]]
    """
    List of tags for the Load Balancer.
    """
    
    capacity: Optional[UpdateInstanceGroupRequestCapacity]
    """
    Specification of the minimum and maximum replicas for the Instance group, and the cooldown interval between two scaling events.
    """
    
    loadbalancer: Optional[UpdateInstanceGroupRequestLoadbalancer]
    """
    Specification of the Load Balancer to link to the Instance group.
    """
    

@dataclass
class UpdateInstancePolicyRequest:
    policy_id: str
    """
    Policy ID to update.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    name: Optional[str]
    """
    Policy name to update.
    """
    
    action: Optional[InstancePolicyAction]
    """
    Action to update (action to execute when the metric-based condition is met).
    """
    
    type_: Optional[InstancePolicyType]
    """
    Type to update (how to use the number defined in `value` when determining by how many Instances to scale up/down).
    """
    
    value: Optional[int]
    """
    Value to update (number representing the magnitude of the scaling action to take for the Instance group).
    """
    
    priority: Optional[int]
    """
    Priority to update (priority of this policy compared to all other scaling policies. The lower the number, the higher the priority).
    """
    
    metric: Optional[UpdateInstancePolicyRequestMetric]
    

@dataclass
class UpdateInstanceTemplateRequest:
    template_id: str
    """
    Template ID of the resource.
    """
    
    zone: Optional[ScwZone]
    """
    Zone to target. If none is passed will use default zone from the config.
    """
    
    commercial_type: Optional[str]
    """
    Name of Instance commercial type.
    """
    
    image_id: Optional[str]
    """
    Instance image ID. Can be an ID of a marketplace or personal image. This image must be compatible with `volume` and `commercial_type` template.
    """
    
    volumes: Optional[Dict[str, VolumeInstanceTemplate]]
    """
    Template of Instance volume.
    """
    
    tags: Optional[List[str]]
    """
    List of tags for the Instance template.
    """
    
    security_group_id: Optional[str]
    """
    Instance security group ID (optional).
    """
    
    placement_group_id: Optional[str]
    """
    Instance placement group ID. This is optional, but it is highly recommended to set a preference for Instance location within Availability Zone.
    """
    
    public_ips_v4_count: Optional[int]
    """
    Number of flexible IPv4 addresses to attach to the new Instance.
    """
    
    public_ips_v6_count: Optional[int]
    """
    Number of flexible IPv6 addresses to attach to the new Instance.
    """
    
    name: Optional[str]
    """
    Name of Instance template.
    """
    
    private_network_ids: Optional[List[str]]
    """
    Private Network IDs to attach to the new Instance.
    """
    
    cloud_init: Optional[str]
    """
    Cloud-config file must be passed in Base64 format. Cloud-config files are special scripts designed to be run by the cloud-init process. These are generally used for initial configuration on the very first boot of a server.
    """
    
