# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types import (
    AclActionRedirectRedirectType,
    AclActionType,
    AclHttpFilter,
    BackendServerStatsHealthCheckStatus,
    BackendServerStatsServerState,
    CertificateStatus,
    CertificateType,
    ForwardPortAlgorithm,
    InstanceStatus,
    LbStatus,
    LbTypeStock,
    ListAclRequestOrderBy,
    ListBackendsRequestOrderBy,
    ListCertificatesRequestOrderBy,
    ListFrontendsRequestOrderBy,
    ListIpsRequestIpType,
    ListLbsRequestOrderBy,
    ListPrivateNetworksRequestOrderBy,
    ListRoutesRequestOrderBy,
    ListSubscriberRequestOrderBy,
    OnMarkedDownAction,
    PrivateNetworkStatus,
    Protocol,
    ProxyProtocol,
    SSLCompatibilityLevel,
    StickySessionsType,
    Ip,
    SubscriberEmailConfig,
    SubscriberWebhookConfig,
    Subscriber,
    HealthCheckHttpConfig,
    HealthCheckHttpsConfig,
    HealthCheckLdapConfig,
    HealthCheckMysqlConfig,
    HealthCheckPgsqlConfig,
    HealthCheckRedisConfig,
    HealthCheckTcpConfig,
    HealthCheck,
    Instance,
    Lb,
    Backend,
    Certificate,
    Frontend,
    AclActionRedirect,
    AclAction,
    AclMatch,
    Acl,
    PrivateNetworkDHCPConfig,
    PrivateNetworkIpamConfig,
    PrivateNetworkStaticConfig,
    PrivateNetwork,
    RouteMatch,
    Route,
    BackendServerStats,
    LbStats,
    ListAclResponse,
    ListBackendStatsResponse,
    ListBackendsResponse,
    ListCertificatesResponse,
    ListFrontendsResponse,
    ListIpsResponse,
    ListLbPrivateNetworksResponse,
    LbType,
    ListLbTypesResponse,
    ListLbsResponse,
    ListRoutesResponse,
    ListSubscriberResponse,
    SetAclsResponse,
    AddBackendServersRequest,
    AttachPrivateNetworkRequest,
    CreateAclRequest,
    CreateBackendRequest,
    CreateCertificateRequestCustomCertificate,
    CreateCertificateRequestLetsencryptConfig,
    CreateCertificateRequest,
    CreateFrontendRequest,
    CreateIpRequest,
    CreateLbRequest,
    CreateRouteRequest,
    CreateSubscriberRequest,
    MigrateLbRequest,
    RemoveBackendServersRequest,
    SetBackendServersRequest,
    SubscribeToLbRequest,
    UpdateAclRequest,
    UpdateBackendRequest,
    UpdateCertificateRequest,
    UpdateFrontendRequest,
    UpdateHealthCheckRequest,
    UpdateIpRequest,
    UpdateLbRequest,
    UpdateRouteRequest,
    UpdateSubscriberRequest,
    ZonedApiAddBackendServersRequest,
    ZonedApiAttachPrivateNetworkRequest,
    ZonedApiCreateAclRequest,
    ZonedApiCreateBackendRequest,
    ZonedApiCreateCertificateRequest,
    ZonedApiCreateFrontendRequest,
    ZonedApiCreateIpRequest,
    ZonedApiCreateLbRequest,
    ZonedApiCreateRouteRequest,
    ZonedApiCreateSubscriberRequest,
    ZonedApiDetachPrivateNetworkRequest,
    ZonedApiMigrateLbRequest,
    ZonedApiRemoveBackendServersRequest,
    AclSpec,
    ZonedApiSetAclsRequest,
    ZonedApiSetBackendServersRequest,
    ZonedApiSubscribeToLbRequest,
    ZonedApiUpdateAclRequest,
    ZonedApiUpdateBackendRequest,
    ZonedApiUpdateCertificateRequest,
    ZonedApiUpdateFrontendRequest,
    ZonedApiUpdateHealthCheckRequest,
    ZonedApiUpdateIpRequest,
    ZonedApiUpdateLbRequest,
    ZonedApiUpdateRouteRequest,
    ZonedApiUpdateSubscriberRequest,
)

def unmarshal_Ip(data: Any) -> Ip:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Ip' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("ip_address", str())
    args["ip_address"] = field

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("reverse", str())
    args["reverse"] = field

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("lb_id", None)
    args["lb_id"] = field

    field = data.get("region", None)
    args["region"] = field

    return Ip(**args)

def unmarshal_SubscriberEmailConfig(data: Any) -> SubscriberEmailConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscriberEmailConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("email", str())
    args["email"] = field

    return SubscriberEmailConfig(**args)

def unmarshal_SubscriberWebhookConfig(data: Any) -> SubscriberWebhookConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SubscriberWebhookConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("uri", str())
    args["uri"] = field

    return SubscriberWebhookConfig(**args)

def unmarshal_Subscriber(data: Any) -> Subscriber:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Subscriber' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("email_config", None)
    args["email_config"] = unmarshal_SubscriberEmailConfig(field) if field is not None else None

    field = data.get("webhook_config", None)
    args["webhook_config"] = unmarshal_SubscriberWebhookConfig(field) if field is not None else None

    return Subscriber(**args)

def unmarshal_HealthCheckHttpConfig(data: Any) -> HealthCheckHttpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckHttpConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("uri", str())
    args["uri"] = field

    field = data.get("method", str())
    args["method"] = field

    field = data.get("host_header", str())
    args["host_header"] = field

    field = data.get("code", None)
    args["code"] = field

    return HealthCheckHttpConfig(**args)

def unmarshal_HealthCheckHttpsConfig(data: Any) -> HealthCheckHttpsConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckHttpsConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("uri", str())
    args["uri"] = field

    field = data.get("method", str())
    args["method"] = field

    field = data.get("host_header", str())
    args["host_header"] = field

    field = data.get("sni", str())
    args["sni"] = field

    field = data.get("code", None)
    args["code"] = field

    return HealthCheckHttpsConfig(**args)

def unmarshal_HealthCheckLdapConfig(data: Any) -> HealthCheckLdapConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckLdapConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return HealthCheckLdapConfig(**args)

def unmarshal_HealthCheckMysqlConfig(data: Any) -> HealthCheckMysqlConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckMysqlConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user", str())
    args["user"] = field

    return HealthCheckMysqlConfig(**args)

def unmarshal_HealthCheckPgsqlConfig(data: Any) -> HealthCheckPgsqlConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckPgsqlConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("user", str())
    args["user"] = field

    return HealthCheckPgsqlConfig(**args)

def unmarshal_HealthCheckRedisConfig(data: Any) -> HealthCheckRedisConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckRedisConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return HealthCheckRedisConfig(**args)

def unmarshal_HealthCheckTcpConfig(data: Any) -> HealthCheckTcpConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheckTcpConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return HealthCheckTcpConfig(**args)

def unmarshal_HealthCheck(data: Any) -> HealthCheck:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'HealthCheck' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("port", 0)
    args["port"] = field

    field = data.get("check_max_retries", 0)
    args["check_max_retries"] = field

    field = data.get("check_delay", None)
    args["check_delay"] = field

    field = data.get("check_timeout", None)
    args["check_timeout"] = field

    field = data.get("tcp_config", None)
    args["tcp_config"] = unmarshal_HealthCheckTcpConfig(field) if field is not None else None

    field = data.get("mysql_config", None)
    args["mysql_config"] = unmarshal_HealthCheckMysqlConfig(field) if field is not None else None

    field = data.get("check_send_proxy", False)
    args["check_send_proxy"] = field

    field = data.get("pgsql_config", None)
    args["pgsql_config"] = unmarshal_HealthCheckPgsqlConfig(field) if field is not None else None

    field = data.get("ldap_config", None)
    args["ldap_config"] = unmarshal_HealthCheckLdapConfig(field) if field is not None else None

    field = data.get("redis_config", None)
    args["redis_config"] = unmarshal_HealthCheckRedisConfig(field) if field is not None else None

    field = data.get("http_config", None)
    args["http_config"] = unmarshal_HealthCheckHttpConfig(field) if field is not None else None

    field = data.get("https_config", None)
    args["https_config"] = unmarshal_HealthCheckHttpsConfig(field) if field is not None else None

    field = data.get("transient_check_delay", None)
    args["transient_check_delay"] = field

    return HealthCheck(**args)

def unmarshal_Instance(data: Any) -> Instance:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Instance' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("status", getattr(InstanceStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("ip_address", str())
    args["ip_address"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("region", None)
    args["region"] = field

    return Instance(**args)

def unmarshal_Lb(data: Any) -> Lb:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Lb' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("status", getattr(LbStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("instances", [])
    args["instances"] = [unmarshal_Instance(v) for v in field] if field is not None else None

    field = data.get("organization_id", str())
    args["organization_id"] = field

    field = data.get("project_id", str())
    args["project_id"] = field

    field = data.get("ip", [])
    args["ip"] = [unmarshal_Ip(v) for v in field] if field is not None else None

    field = data.get("tags", [])
    args["tags"] = field

    field = data.get("frontend_count", 0)
    args["frontend_count"] = field

    field = data.get("backend_count", 0)
    args["backend_count"] = field

    field = data.get("type", str())
    args["type_"] = field

    field = data.get("ssl_compatibility_level", getattr(SSLCompatibilityLevel, "SSL_COMPATIBILITY_LEVEL_UNKNOWN"))
    args["ssl_compatibility_level"] = field

    field = data.get("private_network_count", 0)
    args["private_network_count"] = field

    field = data.get("route_count", 0)
    args["route_count"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("subscriber", None)
    args["subscriber"] = unmarshal_Subscriber(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("region", None)
    args["region"] = field

    return Lb(**args)

def unmarshal_Backend(data: Any) -> Backend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Backend' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("forward_protocol", getattr(Protocol, "TCP"))
    args["forward_protocol"] = field

    field = data.get("forward_port", 0)
    args["forward_port"] = field

    field = data.get("forward_port_algorithm", getattr(ForwardPortAlgorithm, "ROUNDROBIN"))
    args["forward_port_algorithm"] = field

    field = data.get("sticky_sessions", getattr(StickySessionsType, "NONE"))
    args["sticky_sessions"] = field

    field = data.get("sticky_sessions_cookie_name", str())
    args["sticky_sessions_cookie_name"] = field

    field = data.get("pool", [])
    args["pool"] = field

    field = data.get("on_marked_down_action", getattr(OnMarkedDownAction, "ON_MARKED_DOWN_ACTION_NONE"))
    args["on_marked_down_action"] = field

    field = data.get("proxy_protocol", getattr(ProxyProtocol, "PROXY_PROTOCOL_UNKNOWN"))
    args["proxy_protocol"] = field

    field = data.get("health_check", None)
    args["health_check"] = unmarshal_HealthCheck(field) if field is not None else None

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("send_proxy_v2", None)
    args["send_proxy_v2"] = field

    field = data.get("timeout_server", None)
    args["timeout_server"] = field

    field = data.get("timeout_connect", None)
    args["timeout_connect"] = field

    field = data.get("timeout_tunnel", None)
    args["timeout_tunnel"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("failover_host", None)
    args["failover_host"] = field

    field = data.get("ssl_bridging", None)
    args["ssl_bridging"] = field

    field = data.get("ignore_ssl_server_verify", None)
    args["ignore_ssl_server_verify"] = field

    field = data.get("redispatch_attempt_count", None)
    args["redispatch_attempt_count"] = field

    field = data.get("max_retries", None)
    args["max_retries"] = field

    field = data.get("max_connections", None)
    args["max_connections"] = field

    field = data.get("timeout_queue", None)
    args["timeout_queue"] = field

    return Backend(**args)

def unmarshal_Certificate(data: Any) -> Certificate:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Certificate' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(CertificateType, "LETSENCRYT"))
    args["type_"] = field

    field = data.get("id", str())
    args["id"] = field

    field = data.get("common_name", str())
    args["common_name"] = field

    field = data.get("subject_alternative_name", [])
    args["subject_alternative_name"] = field

    field = data.get("fingerprint", str())
    args["fingerprint"] = field

    field = data.get("status", getattr(CertificateStatus, "PENDING"))
    args["status"] = field

    field = data.get("not_valid_before", None)
    args["not_valid_before"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("not_valid_after", None)
    args["not_valid_after"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("name", str())
    args["name"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("status_details", None)
    args["status_details"] = field

    return Certificate(**args)

def unmarshal_Frontend(data: Any) -> Frontend:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Frontend' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("inbound_port", 0)
    args["inbound_port"] = field

    field = data.get("certificate_ids", [])
    args["certificate_ids"] = field

    field = data.get("backend", None)
    args["backend"] = unmarshal_Backend(field) if field is not None else None

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("timeout_client", None)
    args["timeout_client"] = field

    field = data.get("enable_http3", False)
    args["enable_http3"] = field

    field = data.get("enable_access_logs", False)
    args["enable_access_logs"] = field

    field = data.get("certificate", None)
    args["certificate"] = unmarshal_Certificate(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("connection_rate_limit", None)
    args["connection_rate_limit"] = field

    return Frontend(**args)

def unmarshal_AclActionRedirect(data: Any) -> AclActionRedirect:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclActionRedirect' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(AclActionRedirectRedirectType, "LOCATION"))
    args["type_"] = field

    field = data.get("target", str())
    args["target"] = field

    field = data.get("code", None)
    args["code"] = field

    return AclActionRedirect(**args)

def unmarshal_AclAction(data: Any) -> AclAction:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclAction' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(AclActionType, "ALLOW"))
    args["type_"] = field

    field = data.get("redirect", None)
    args["redirect"] = unmarshal_AclActionRedirect(field) if field is not None else None

    return AclAction(**args)

def unmarshal_AclMatch(data: Any) -> AclMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'AclMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_subnet", [])
    args["ip_subnet"] = field

    field = data.get("ips_edge_services", False)
    args["ips_edge_services"] = field

    field = data.get("http_filter", getattr(AclHttpFilter, "ACL_HTTP_FILTER_NONE"))
    args["http_filter"] = field

    field = data.get("http_filter_value", [])
    args["http_filter_value"] = field

    field = data.get("invert", False)
    args["invert"] = field

    field = data.get("http_filter_option", None)
    args["http_filter_option"] = field

    return AclMatch(**args)

def unmarshal_Acl(data: Any) -> Acl:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Acl' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("name", str())
    args["name"] = field

    field = data.get("index", 0)
    args["index"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("match", None)
    args["match"] = unmarshal_AclMatch(field) if field is not None else None

    field = data.get("action", None)
    args["action"] = unmarshal_AclAction(field) if field is not None else None

    field = data.get("frontend", None)
    args["frontend"] = unmarshal_Frontend(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Acl(**args)

def unmarshal_PrivateNetworkDHCPConfig(data: Any) -> PrivateNetworkDHCPConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkDHCPConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_id", None)
    args["ip_id"] = field

    return PrivateNetworkDHCPConfig(**args)

def unmarshal_PrivateNetworkIpamConfig(data: Any) -> PrivateNetworkIpamConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkIpamConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return PrivateNetworkIpamConfig(**args)

def unmarshal_PrivateNetworkStaticConfig(data: Any) -> PrivateNetworkStaticConfig:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetworkStaticConfig' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_address", None)
    args["ip_address"] = field

    return PrivateNetworkStaticConfig(**args)

def unmarshal_PrivateNetwork(data: Any) -> PrivateNetwork:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PrivateNetwork' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ipam_ids", [])
    args["ipam_ids"] = field

    field = data.get("private_network_id", str())
    args["private_network_id"] = field

    field = data.get("status", getattr(PrivateNetworkStatus, "UNKNOWN"))
    args["status"] = field

    field = data.get("lb", None)
    args["lb"] = unmarshal_Lb(field) if field is not None else None

    field = data.get("static_config", None)
    args["static_config"] = unmarshal_PrivateNetworkStaticConfig(field) if field is not None else None

    field = data.get("dhcp_config", None)
    args["dhcp_config"] = unmarshal_PrivateNetworkDHCPConfig(field) if field is not None else None

    field = data.get("ipam_config", None)
    args["ipam_config"] = unmarshal_PrivateNetworkIpamConfig(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return PrivateNetwork(**args)

def unmarshal_RouteMatch(data: Any) -> RouteMatch:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'RouteMatch' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("match_subdomains", False)
    args["match_subdomains"] = field

    field = data.get("sni", None)
    args["sni"] = field

    field = data.get("host_header", None)
    args["host_header"] = field

    field = data.get("path_begin", None)
    args["path_begin"] = field

    return RouteMatch(**args)

def unmarshal_Route(data: Any) -> Route:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Route' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", str())
    args["id"] = field

    field = data.get("frontend_id", str())
    args["frontend_id"] = field

    field = data.get("backend_id", str())
    args["backend_id"] = field

    field = data.get("match", None)
    args["match"] = unmarshal_RouteMatch(field) if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return Route(**args)

def unmarshal_BackendServerStats(data: Any) -> BackendServerStats:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'BackendServerStats' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("instance_id", str())
    args["instance_id"] = field

    field = data.get("backend_id", str())
    args["backend_id"] = field

    field = data.get("ip", str())
    args["ip"] = field

    field = data.get("server_state", getattr(BackendServerStatsServerState, "STOPPED"))
    args["server_state"] = field

    field = data.get("last_health_check_status", getattr(BackendServerStatsHealthCheckStatus, "UNKNOWN"))
    args["last_health_check_status"] = field

    field = data.get("server_state_changed_at", None)
    args["server_state_changed_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return BackendServerStats(**args)

def unmarshal_LbStats(data: Any) -> LbStats:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LbStats' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_servers_stats", [])
    args["backend_servers_stats"] = [unmarshal_BackendServerStats(v) for v in field] if field is not None else None

    return LbStats(**args)

def unmarshal_ListAclResponse(data: Any) -> ListAclResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListAclResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acls", [])
    args["acls"] = [unmarshal_Acl(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListAclResponse(**args)

def unmarshal_ListBackendStatsResponse(data: Any) -> ListBackendStatsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendStatsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backend_servers_stats", [])
    args["backend_servers_stats"] = [unmarshal_BackendServerStats(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListBackendStatsResponse(**args)

def unmarshal_ListBackendsResponse(data: Any) -> ListBackendsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListBackendsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("backends", [])
    args["backends"] = [unmarshal_Backend(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListBackendsResponse(**args)

def unmarshal_ListCertificatesResponse(data: Any) -> ListCertificatesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCertificatesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("certificates", [])
    args["certificates"] = [unmarshal_Certificate(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListCertificatesResponse(**args)

def unmarshal_ListFrontendsResponse(data: Any) -> ListFrontendsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListFrontendsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("frontends", [])
    args["frontends"] = [unmarshal_Frontend(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListFrontendsResponse(**args)

def unmarshal_ListIpsResponse(data: Any) -> ListIpsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListIpsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ips", [])
    args["ips"] = [unmarshal_Ip(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListIpsResponse(**args)

def unmarshal_ListLbPrivateNetworksResponse(data: Any) -> ListLbPrivateNetworksResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbPrivateNetworksResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("private_network", [])
    args["private_network"] = [unmarshal_PrivateNetwork(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListLbPrivateNetworksResponse(**args)

def unmarshal_LbType(data: Any) -> LbType:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'LbType' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("name", str())
    args["name"] = field

    field = data.get("stock_status", getattr(LbTypeStock, "UNKNOWN"))
    args["stock_status"] = field

    field = data.get("description", str())
    args["description"] = field

    field = data.get("zone", )
    args["zone"] = field

    field = data.get("region", None)
    args["region"] = field

    return LbType(**args)

def unmarshal_ListLbTypesResponse(data: Any) -> ListLbTypesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbTypesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("lb_types", [])
    args["lb_types"] = [unmarshal_LbType(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListLbTypesResponse(**args)

def unmarshal_ListLbsResponse(data: Any) -> ListLbsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListLbsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("lbs", [])
    args["lbs"] = [unmarshal_Lb(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListLbsResponse(**args)

def unmarshal_ListRoutesResponse(data: Any) -> ListRoutesResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListRoutesResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("routes", [])
    args["routes"] = [unmarshal_Route(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListRoutesResponse(**args)

def unmarshal_ListSubscriberResponse(data: Any) -> ListSubscriberResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListSubscriberResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("subscribers", [])
    args["subscribers"] = [unmarshal_Subscriber(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return ListSubscriberResponse(**args)

def unmarshal_SetAclsResponse(data: Any) -> SetAclsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'SetAclsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("acls", [])
    args["acls"] = [unmarshal_Acl(v) for v in field] if field is not None else None

    field = data.get("total_count", 0)
    args["total_count"] = field

    return SetAclsResponse(**args)

def marshal_AddBackendServersRequest(
    request: AddBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()


    return output

def marshal_PrivateNetworkDHCPConfig(
    request: PrivateNetworkDHCPConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id
    else:
        output["ip_id"] = None


    return output

def marshal_PrivateNetworkIpamConfig(
    request: PrivateNetworkIpamConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_PrivateNetworkStaticConfig(
    request: PrivateNetworkStaticConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_address is not None:
        output["ip_address"] = request.ip_address
    else:
        output["ip_address"] = None


    return output

def marshal_AttachPrivateNetworkRequest(
    request: AttachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="static_config", value=request.static_config,marshal_func=marshal_PrivateNetworkStaticConfig
            ),
            OneOfPossibility(param="dhcp_config", value=request.dhcp_config,marshal_func=marshal_PrivateNetworkDHCPConfig
            ),
            OneOfPossibility(param="ipam_config", value=request.ipam_config,marshal_func=marshal_PrivateNetworkIpamConfig
            ),
        ]),
    )

    if request.ipam_ids is not None:
        output["ipam_ids"] = request.ipam_ids
    else:
        output["ipam_ids"] = None


    return output

def marshal_AclActionRedirect(
    request: AclActionRedirect,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = getattr(AclActionRedirectRedirectType, "LOCATION")

    if request.target is not None:
        output["target"] = request.target
    else:
        output["target"] = str()

    if request.code is not None:
        output["code"] = request.code
    else:
        output["code"] = None


    return output

def marshal_AclAction(
    request: AclAction,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = getattr(AclActionType, "ALLOW")

    if request.redirect is not None:
        output["redirect"] = marshal_AclActionRedirect(request.redirect, defaults)
    else:
        output["redirect"] = None


    return output

def marshal_AclMatch(
    request: AclMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_subnet is not None:
        output["ip_subnet"] = request.ip_subnet
    else:
        output["ip_subnet"] = []

    if request.ips_edge_services is not None:
        output["ips_edge_services"] = request.ips_edge_services
    else:
        output["ips_edge_services"] = False

    if request.http_filter is not None:
        output["http_filter"] = str(request.http_filter)
    else:
        output["http_filter"] = getattr(AclHttpFilter, "ACL_HTTP_FILTER_NONE")

    if request.http_filter_value is not None:
        output["http_filter_value"] = request.http_filter_value
    else:
        output["http_filter_value"] = []

    if request.invert is not None:
        output["invert"] = request.invert
    else:
        output["invert"] = False

    if request.http_filter_option is not None:
        output["http_filter_option"] = request.http_filter_option
    else:
        output["http_filter_option"] = None


    return output

def marshal_CreateAclRequest(
    request: CreateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)
    else:
        output["action"] = str()

    if request.index is not None:
        output["index"] = request.index
    else:
        output["index"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_HealthCheckHttpConfig(
    request: HealthCheckHttpConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri
    else:
        output["uri"] = str()

    if request.method is not None:
        output["method"] = request.method
    else:
        output["method"] = str()

    if request.host_header is not None:
        output["host_header"] = request.host_header
    else:
        output["host_header"] = str()

    if request.code is not None:
        output["code"] = request.code
    else:
        output["code"] = None


    return output

def marshal_HealthCheckHttpsConfig(
    request: HealthCheckHttpsConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri
    else:
        output["uri"] = str()

    if request.method is not None:
        output["method"] = request.method
    else:
        output["method"] = str()

    if request.host_header is not None:
        output["host_header"] = request.host_header
    else:
        output["host_header"] = str()

    if request.sni is not None:
        output["sni"] = request.sni
    else:
        output["sni"] = str()

    if request.code is not None:
        output["code"] = request.code
    else:
        output["code"] = None


    return output

def marshal_HealthCheckLdapConfig(
    request: HealthCheckLdapConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_HealthCheckMysqlConfig(
    request: HealthCheckMysqlConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user is not None:
        output["user"] = request.user
    else:
        output["user"] = str()


    return output

def marshal_HealthCheckPgsqlConfig(
    request: HealthCheckPgsqlConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.user is not None:
        output["user"] = request.user
    else:
        output["user"] = str()


    return output

def marshal_HealthCheckRedisConfig(
    request: HealthCheckRedisConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_HealthCheckTcpConfig(
    request: HealthCheckTcpConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}


    return output

def marshal_HealthCheck(
    request: HealthCheck,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="tcp_config", value=request.tcp_config,marshal_func=marshal_HealthCheckTcpConfig
            ),
            OneOfPossibility(param="mysql_config", value=request.mysql_config,marshal_func=marshal_HealthCheckMysqlConfig
            ),
            OneOfPossibility(param="pgsql_config", value=request.pgsql_config,marshal_func=marshal_HealthCheckPgsqlConfig
            ),
            OneOfPossibility(param="ldap_config", value=request.ldap_config,marshal_func=marshal_HealthCheckLdapConfig
            ),
            OneOfPossibility(param="redis_config", value=request.redis_config,marshal_func=marshal_HealthCheckRedisConfig
            ),
            OneOfPossibility(param="http_config", value=request.http_config,marshal_func=marshal_HealthCheckHttpConfig
            ),
            OneOfPossibility(param="https_config", value=request.https_config,marshal_func=marshal_HealthCheckHttpsConfig
            ),
        ]),
    )

    if request.port is not None:
        output["port"] = request.port
    else:
        output["port"] = 0

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries
    else:
        output["check_max_retries"] = 0

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy
    else:
        output["check_send_proxy"] = False

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay
    else:
        output["check_delay"] = None

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout
    else:
        output["check_timeout"] = None

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay
    else:
        output["transient_check_delay"] = None


    return output

def marshal_CreateBackendRequest(
    request: CreateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.forward_protocol is not None:
        output["forward_protocol"] = str(request.forward_protocol)
    else:
        output["forward_protocol"] = str()

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port
    else:
        output["forward_port"] = str()

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = str(request.forward_port_algorithm)
    else:
        output["forward_port_algorithm"] = str()

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = str(request.sticky_sessions)
    else:
        output["sticky_sessions"] = str()

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name
    else:
        output["sticky_sessions_cookie_name"] = str()

    if request.health_check is not None:
        output["health_check"] = marshal_HealthCheck(request.health_check, defaults)
    else:
        output["health_check"] = str()

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2
    else:
        output["send_proxy_v2"] = None

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server
    else:
        output["timeout_server"] = None

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect
    else:
        output["timeout_connect"] = None

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel
    else:
        output["timeout_tunnel"] = None

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = str(request.on_marked_down_action)
    else:
        output["on_marked_down_action"] = None

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = str(request.proxy_protocol)
    else:
        output["proxy_protocol"] = None

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host
    else:
        output["failover_host"] = None

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging
    else:
        output["ssl_bridging"] = None

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify
    else:
        output["ignore_ssl_server_verify"] = None

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count
    else:
        output["redispatch_attempt_count"] = None

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries
    else:
        output["max_retries"] = None

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections
    else:
        output["max_connections"] = None

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue
    else:
        output["timeout_queue"] = None


    return output

def marshal_CreateCertificateRequestCustomCertificate(
    request: CreateCertificateRequestCustomCertificate,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.certificate_chain is not None:
        output["certificate_chain"] = request.certificate_chain
    else:
        output["certificate_chain"] = str()


    return output

def marshal_CreateCertificateRequestLetsencryptConfig(
    request: CreateCertificateRequestLetsencryptConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.common_name is not None:
        output["common_name"] = request.common_name
    else:
        output["common_name"] = str()

    if request.subject_alternative_name is not None:
        output["subject_alternative_name"] = request.subject_alternative_name
    else:
        output["subject_alternative_name"] = []


    return output

def marshal_CreateCertificateRequest(
    request: CreateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="letsencrypt", value=request.letsencrypt,marshal_func=marshal_CreateCertificateRequestLetsencryptConfig
            ),
            OneOfPossibility(param="custom_certificate", value=request.custom_certificate,marshal_func=marshal_CreateCertificateRequestCustomCertificate
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_CreateFrontendRequest(
    request: CreateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port
    else:
        output["inbound_port"] = str()

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3
    else:
        output["enable_http3"] = False

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs
    else:
        output["enable_access_logs"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client
    else:
        output["timeout_client"] = None

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id
    else:
        output["certificate_id"] = None

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids
    else:
        output["certificate_ids"] = None

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit
    else:
        output["connection_rate_limit"] = None


    return output

def marshal_CreateIpRequest(
    request: CreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6
    else:
        output["is_ipv6"] = False

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_CreateLbRequest(
    request: CreateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id
    else:
        output["ip_id"] = None

    if request.assign_flexible_ip is not None:
        output["assign_flexible_ip"] = request.assign_flexible_ip
    else:
        output["assign_flexible_ip"] = None

    if request.assign_flexible_ipv6 is not None:
        output["assign_flexible_ipv6"] = request.assign_flexible_ipv6
    else:
        output["assign_flexible_ipv6"] = None

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids
    else:
        output["ip_ids"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = str(request.ssl_compatibility_level)
    else:
        output["ssl_compatibility_level"] = None


    return output

def marshal_RouteMatch(
    request: RouteMatch,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="sni", value=request.sni,marshal_func=None
            ),
            OneOfPossibility(param="host_header", value=request.host_header,marshal_func=None
            ),
            OneOfPossibility(param="path_begin", value=request.path_begin,marshal_func=None
            ),
        ]),
    )

    if request.match_subdomains is not None:
        output["match_subdomains"] = request.match_subdomains
    else:
        output["match_subdomains"] = False


    return output

def marshal_CreateRouteRequest(
    request: CreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id
    else:
        output["frontend_id"] = str()

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_SubscriberEmailConfig(
    request: SubscriberEmailConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email
    else:
        output["email"] = str()


    return output

def marshal_SubscriberWebhookConfig(
    request: SubscriberWebhookConfig,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.uri is not None:
        output["uri"] = request.uri
    else:
        output["uri"] = str()


    return output

def marshal_CreateSubscriberRequest(
    request: CreateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email_config", value=request.email_config,marshal_func=marshal_SubscriberEmailConfig
            ),
            OneOfPossibility(param="webhook_config", value=request.webhook_config,marshal_func=marshal_SubscriberWebhookConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_MigrateLbRequest(
    request: MigrateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()


    return output

def marshal_RemoveBackendServersRequest(
    request: RemoveBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()


    return output

def marshal_SetBackendServersRequest(
    request: SetBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()


    return output

def marshal_SubscribeToLbRequest(
    request: SubscribeToLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subscriber_id is not None:
        output["subscriber_id"] = request.subscriber_id
    else:
        output["subscriber_id"] = str()


    return output

def marshal_UpdateAclRequest(
    request: UpdateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)
    else:
        output["action"] = str()

    if request.index is not None:
        output["index"] = request.index
    else:
        output["index"] = str()

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)
    else:
        output["match"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_UpdateBackendRequest(
    request: UpdateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.forward_protocol is not None:
        output["forward_protocol"] = str(request.forward_protocol)
    else:
        output["forward_protocol"] = str()

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port
    else:
        output["forward_port"] = str()

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = str(request.forward_port_algorithm)
    else:
        output["forward_port_algorithm"] = str()

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = str(request.sticky_sessions)
    else:
        output["sticky_sessions"] = str()

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name
    else:
        output["sticky_sessions_cookie_name"] = str()

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2
    else:
        output["send_proxy_v2"] = None

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server
    else:
        output["timeout_server"] = None

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect
    else:
        output["timeout_connect"] = None

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel
    else:
        output["timeout_tunnel"] = None

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = str(request.on_marked_down_action)
    else:
        output["on_marked_down_action"] = None

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = str(request.proxy_protocol)
    else:
        output["proxy_protocol"] = None

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host
    else:
        output["failover_host"] = None

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging
    else:
        output["ssl_bridging"] = None

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify
    else:
        output["ignore_ssl_server_verify"] = None

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count
    else:
        output["redispatch_attempt_count"] = None

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries
    else:
        output["max_retries"] = None

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections
    else:
        output["max_connections"] = None

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue
    else:
        output["timeout_queue"] = None


    return output

def marshal_UpdateCertificateRequest(
    request: UpdateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_UpdateFrontendRequest(
    request: UpdateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port
    else:
        output["inbound_port"] = str()

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3
    else:
        output["enable_http3"] = False

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client
    else:
        output["timeout_client"] = None

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id
    else:
        output["certificate_id"] = None

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids
    else:
        output["certificate_ids"] = None

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit
    else:
        output["connection_rate_limit"] = None

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs
    else:
        output["enable_access_logs"] = None


    return output

def marshal_UpdateHealthCheckRequest(
    request: UpdateHealthCheckRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="tcp_config", value=request.tcp_config,marshal_func=marshal_HealthCheckTcpConfig
            ),
            OneOfPossibility(param="mysql_config", value=request.mysql_config,marshal_func=marshal_HealthCheckMysqlConfig
            ),
            OneOfPossibility(param="pgsql_config", value=request.pgsql_config,marshal_func=marshal_HealthCheckPgsqlConfig
            ),
            OneOfPossibility(param="ldap_config", value=request.ldap_config,marshal_func=marshal_HealthCheckLdapConfig
            ),
            OneOfPossibility(param="redis_config", value=request.redis_config,marshal_func=marshal_HealthCheckRedisConfig
            ),
            OneOfPossibility(param="http_config", value=request.http_config,marshal_func=marshal_HealthCheckHttpConfig
            ),
            OneOfPossibility(param="https_config", value=request.https_config,marshal_func=marshal_HealthCheckHttpsConfig
            ),
        ]),
    )

    if request.port is not None:
        output["port"] = request.port
    else:
        output["port"] = str()

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries
    else:
        output["check_max_retries"] = str()

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy
    else:
        output["check_send_proxy"] = False

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay
    else:
        output["check_delay"] = None

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout
    else:
        output["check_timeout"] = None

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay
    else:
        output["transient_check_delay"] = None


    return output

def marshal_UpdateIpRequest(
    request: UpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None

    if request.lb_id is not None:
        output["lb_id"] = request.lb_id
    else:
        output["lb_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_UpdateLbRequest(
    request: UpdateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = str(request.ssl_compatibility_level)
    else:
        output["ssl_compatibility_level"] = None


    return output

def marshal_UpdateRouteRequest(
    request: UpdateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_UpdateSubscriberRequest(
    request: UpdateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email_config", value=request.email_config,marshal_func=marshal_SubscriberEmailConfig
            ),
            OneOfPossibility(param="webhook_config", value=request.webhook_config,marshal_func=marshal_SubscriberWebhookConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_ZonedApiAddBackendServersRequest(
    request: ZonedApiAddBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()


    return output

def marshal_ZonedApiAttachPrivateNetworkRequest(
    request: ZonedApiAttachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="static_config", value=request.static_config,marshal_func=marshal_PrivateNetworkStaticConfig
            ),
            OneOfPossibility(param="dhcp_config", value=request.dhcp_config,marshal_func=marshal_PrivateNetworkDHCPConfig
            ),
            OneOfPossibility(param="ipam_config", value=request.ipam_config,marshal_func=marshal_PrivateNetworkIpamConfig
            ),
        ]),
    )

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()

    if request.ipam_ids is not None:
        output["ipam_ids"] = request.ipam_ids
    else:
        output["ipam_ids"] = None


    return output

def marshal_ZonedApiCreateAclRequest(
    request: ZonedApiCreateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)
    else:
        output["action"] = str()

    if request.index is not None:
        output["index"] = request.index
    else:
        output["index"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_ZonedApiCreateBackendRequest(
    request: ZonedApiCreateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.forward_protocol is not None:
        output["forward_protocol"] = str(request.forward_protocol)
    else:
        output["forward_protocol"] = str()

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port
    else:
        output["forward_port"] = str()

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = str(request.forward_port_algorithm)
    else:
        output["forward_port_algorithm"] = str()

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = str(request.sticky_sessions)
    else:
        output["sticky_sessions"] = str()

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name
    else:
        output["sticky_sessions_cookie_name"] = str()

    if request.health_check is not None:
        output["health_check"] = marshal_HealthCheck(request.health_check, defaults)
    else:
        output["health_check"] = str()

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2
    else:
        output["send_proxy_v2"] = None

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server
    else:
        output["timeout_server"] = None

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect
    else:
        output["timeout_connect"] = None

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel
    else:
        output["timeout_tunnel"] = None

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = str(request.on_marked_down_action)
    else:
        output["on_marked_down_action"] = None

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = str(request.proxy_protocol)
    else:
        output["proxy_protocol"] = None

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host
    else:
        output["failover_host"] = None

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging
    else:
        output["ssl_bridging"] = None

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify
    else:
        output["ignore_ssl_server_verify"] = None

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count
    else:
        output["redispatch_attempt_count"] = None

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries
    else:
        output["max_retries"] = None

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections
    else:
        output["max_connections"] = None

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue
    else:
        output["timeout_queue"] = None


    return output

def marshal_ZonedApiCreateCertificateRequest(
    request: ZonedApiCreateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="letsencrypt", value=request.letsencrypt,marshal_func=marshal_CreateCertificateRequestLetsencryptConfig
            ),
            OneOfPossibility(param="custom_certificate", value=request.custom_certificate,marshal_func=marshal_CreateCertificateRequestCustomCertificate
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None


    return output

def marshal_ZonedApiCreateFrontendRequest(
    request: ZonedApiCreateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port
    else:
        output["inbound_port"] = str()

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3
    else:
        output["enable_http3"] = False

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs
    else:
        output["enable_access_logs"] = False

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client
    else:
        output["timeout_client"] = None

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id
    else:
        output["certificate_id"] = None

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids
    else:
        output["certificate_ids"] = None

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit
    else:
        output["connection_rate_limit"] = None


    return output

def marshal_ZonedApiCreateIpRequest(
    request: ZonedApiCreateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.is_ipv6 is not None:
        output["is_ipv6"] = request.is_ipv6
    else:
        output["is_ipv6"] = False

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_ZonedApiCreateLbRequest(
    request: ZonedApiCreateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = None

    if request.ip_id is not None:
        output["ip_id"] = request.ip_id
    else:
        output["ip_id"] = None

    if request.assign_flexible_ip is not None:
        output["assign_flexible_ip"] = request.assign_flexible_ip
    else:
        output["assign_flexible_ip"] = None

    if request.assign_flexible_ipv6 is not None:
        output["assign_flexible_ipv6"] = request.assign_flexible_ipv6
    else:
        output["assign_flexible_ipv6"] = None

    if request.ip_ids is not None:
        output["ip_ids"] = request.ip_ids
    else:
        output["ip_ids"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = str(request.ssl_compatibility_level)
    else:
        output["ssl_compatibility_level"] = None


    return output

def marshal_ZonedApiCreateRouteRequest(
    request: ZonedApiCreateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.frontend_id is not None:
        output["frontend_id"] = request.frontend_id
    else:
        output["frontend_id"] = str()

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_ZonedApiCreateSubscriberRequest(
    request: ZonedApiCreateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="project_id", value=request.project_id, default=defaults.default_project_id,marshal_func=None
            ),
            OneOfPossibility(param="organization_id", value=request.organization_id,default=defaults.default_organization_id,marshal_func=None
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email_config", value=request.email_config,marshal_func=marshal_SubscriberEmailConfig
            ),
            OneOfPossibility(param="webhook_config", value=request.webhook_config,marshal_func=marshal_SubscriberWebhookConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_ZonedApiDetachPrivateNetworkRequest(
    request: ZonedApiDetachPrivateNetworkRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.private_network_id is not None:
        output["private_network_id"] = request.private_network_id
    else:
        output["private_network_id"] = str()


    return output

def marshal_ZonedApiMigrateLbRequest(
    request: ZonedApiMigrateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = request.type_
    else:
        output["type"] = str()


    return output

def marshal_ZonedApiRemoveBackendServersRequest(
    request: ZonedApiRemoveBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()


    return output

def marshal_AclSpec(
    request: AclSpec,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)
    else:
        output["action"] = str()

    if request.index is not None:
        output["index"] = request.index
    else:
        output["index"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_ZonedApiSetAclsRequest(
    request: ZonedApiSetAclsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.acls is not None:
        output["acls"] = [marshal_AclSpec(item, defaults) for item in request.acls]
    else:
        output["acls"] = str()


    return output

def marshal_ZonedApiSetBackendServersRequest(
    request: ZonedApiSetBackendServersRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.server_ip is not None:
        output["server_ip"] = request.server_ip
    else:
        output["server_ip"] = str()


    return output

def marshal_ZonedApiSubscribeToLbRequest(
    request: ZonedApiSubscribeToLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subscriber_id is not None:
        output["subscriber_id"] = request.subscriber_id
    else:
        output["subscriber_id"] = str()


    return output

def marshal_ZonedApiUpdateAclRequest(
    request: ZonedApiUpdateAclRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.action is not None:
        output["action"] = marshal_AclAction(request.action, defaults)
    else:
        output["action"] = str()

    if request.index is not None:
        output["index"] = request.index
    else:
        output["index"] = str()

    if request.match is not None:
        output["match"] = marshal_AclMatch(request.match, defaults)
    else:
        output["match"] = None

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = None


    return output

def marshal_ZonedApiUpdateBackendRequest(
    request: ZonedApiUpdateBackendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.forward_protocol is not None:
        output["forward_protocol"] = str(request.forward_protocol)
    else:
        output["forward_protocol"] = str()

    if request.forward_port is not None:
        output["forward_port"] = request.forward_port
    else:
        output["forward_port"] = str()

    if request.forward_port_algorithm is not None:
        output["forward_port_algorithm"] = str(request.forward_port_algorithm)
    else:
        output["forward_port_algorithm"] = str()

    if request.sticky_sessions is not None:
        output["sticky_sessions"] = str(request.sticky_sessions)
    else:
        output["sticky_sessions"] = str()

    if request.sticky_sessions_cookie_name is not None:
        output["sticky_sessions_cookie_name"] = request.sticky_sessions_cookie_name
    else:
        output["sticky_sessions_cookie_name"] = str()

    if request.send_proxy_v2 is not None:
        output["send_proxy_v2"] = request.send_proxy_v2
    else:
        output["send_proxy_v2"] = None

    if request.timeout_server is not None:
        output["timeout_server"] = request.timeout_server
    else:
        output["timeout_server"] = None

    if request.timeout_connect is not None:
        output["timeout_connect"] = request.timeout_connect
    else:
        output["timeout_connect"] = None

    if request.timeout_tunnel is not None:
        output["timeout_tunnel"] = request.timeout_tunnel
    else:
        output["timeout_tunnel"] = None

    if request.on_marked_down_action is not None:
        output["on_marked_down_action"] = str(request.on_marked_down_action)
    else:
        output["on_marked_down_action"] = None

    if request.proxy_protocol is not None:
        output["proxy_protocol"] = str(request.proxy_protocol)
    else:
        output["proxy_protocol"] = None

    if request.failover_host is not None:
        output["failover_host"] = request.failover_host
    else:
        output["failover_host"] = None

    if request.ssl_bridging is not None:
        output["ssl_bridging"] = request.ssl_bridging
    else:
        output["ssl_bridging"] = None

    if request.ignore_ssl_server_verify is not None:
        output["ignore_ssl_server_verify"] = request.ignore_ssl_server_verify
    else:
        output["ignore_ssl_server_verify"] = None

    if request.redispatch_attempt_count is not None:
        output["redispatch_attempt_count"] = request.redispatch_attempt_count
    else:
        output["redispatch_attempt_count"] = None

    if request.max_retries is not None:
        output["max_retries"] = request.max_retries
    else:
        output["max_retries"] = None

    if request.max_connections is not None:
        output["max_connections"] = request.max_connections
    else:
        output["max_connections"] = None

    if request.timeout_queue is not None:
        output["timeout_queue"] = request.timeout_queue
    else:
        output["timeout_queue"] = None


    return output

def marshal_ZonedApiUpdateCertificateRequest(
    request: ZonedApiUpdateCertificateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output

def marshal_ZonedApiUpdateFrontendRequest(
    request: ZonedApiUpdateFrontendRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.inbound_port is not None:
        output["inbound_port"] = request.inbound_port
    else:
        output["inbound_port"] = str()

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.enable_http3 is not None:
        output["enable_http3"] = request.enable_http3
    else:
        output["enable_http3"] = False

    if request.timeout_client is not None:
        output["timeout_client"] = request.timeout_client
    else:
        output["timeout_client"] = None

    if request.certificate_id is not None:
        output["certificate_id"] = request.certificate_id
    else:
        output["certificate_id"] = None

    if request.certificate_ids is not None:
        output["certificate_ids"] = request.certificate_ids
    else:
        output["certificate_ids"] = None

    if request.connection_rate_limit is not None:
        output["connection_rate_limit"] = request.connection_rate_limit
    else:
        output["connection_rate_limit"] = None

    if request.enable_access_logs is not None:
        output["enable_access_logs"] = request.enable_access_logs
    else:
        output["enable_access_logs"] = None


    return output

def marshal_ZonedApiUpdateHealthCheckRequest(
    request: ZonedApiUpdateHealthCheckRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="tcp_config", value=request.tcp_config,marshal_func=marshal_HealthCheckTcpConfig
            ),
            OneOfPossibility(param="mysql_config", value=request.mysql_config,marshal_func=marshal_HealthCheckMysqlConfig
            ),
            OneOfPossibility(param="pgsql_config", value=request.pgsql_config,marshal_func=marshal_HealthCheckPgsqlConfig
            ),
            OneOfPossibility(param="ldap_config", value=request.ldap_config,marshal_func=marshal_HealthCheckLdapConfig
            ),
            OneOfPossibility(param="redis_config", value=request.redis_config,marshal_func=marshal_HealthCheckRedisConfig
            ),
            OneOfPossibility(param="http_config", value=request.http_config,marshal_func=marshal_HealthCheckHttpConfig
            ),
            OneOfPossibility(param="https_config", value=request.https_config,marshal_func=marshal_HealthCheckHttpsConfig
            ),
        ]),
    )

    if request.port is not None:
        output["port"] = request.port
    else:
        output["port"] = str()

    if request.check_max_retries is not None:
        output["check_max_retries"] = request.check_max_retries
    else:
        output["check_max_retries"] = str()

    if request.check_send_proxy is not None:
        output["check_send_proxy"] = request.check_send_proxy
    else:
        output["check_send_proxy"] = False

    if request.check_delay is not None:
        output["check_delay"] = request.check_delay
    else:
        output["check_delay"] = None

    if request.check_timeout is not None:
        output["check_timeout"] = request.check_timeout
    else:
        output["check_timeout"] = None

    if request.transient_check_delay is not None:
        output["transient_check_delay"] = request.transient_check_delay
    else:
        output["transient_check_delay"] = None


    return output

def marshal_ZonedApiUpdateIpRequest(
    request: ZonedApiUpdateIpRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.reverse is not None:
        output["reverse"] = request.reverse
    else:
        output["reverse"] = None

    if request.lb_id is not None:
        output["lb_id"] = request.lb_id
    else:
        output["lb_id"] = None

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_ZonedApiUpdateLbRequest(
    request: ZonedApiUpdateLbRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()

    if request.description is not None:
        output["description"] = request.description
    else:
        output["description"] = str()

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None

    if request.ssl_compatibility_level is not None:
        output["ssl_compatibility_level"] = str(request.ssl_compatibility_level)
    else:
        output["ssl_compatibility_level"] = None


    return output

def marshal_ZonedApiUpdateRouteRequest(
    request: ZonedApiUpdateRouteRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.backend_id is not None:
        output["backend_id"] = request.backend_id
    else:
        output["backend_id"] = str()

    if request.match is not None:
        output["match"] = marshal_RouteMatch(request.match, defaults)
    else:
        output["match"] = None


    return output

def marshal_ZonedApiUpdateSubscriberRequest(
    request: ZonedApiUpdateSubscriberRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="email_config", value=request.email_config,marshal_func=marshal_SubscriberEmailConfig
            ),
            OneOfPossibility(param="webhook_config", value=request.webhook_config,marshal_func=marshal_SubscriberWebhookConfig
            ),
        ]),
    )

    if request.name is not None:
        output["name"] = request.name
    else:
        output["name"] = str()


    return output
