# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from scaleway_core.bridge import (
    Region,
)


class CronStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class DomainStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class FunctionHttpOption(str, Enum):
    UNKNOWN_HTTP_OPTION = "unknown_http_option"
    ENABLED = "enabled"
    REDIRECTED = "redirected"

    def __str__(self) -> str:
        return str(self.value)


class FunctionPrivacy(str, Enum):
    UNKNOWN_PRIVACY = "unknown_privacy"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)


class FunctionRuntime(str, Enum):
    UNKNOWN_RUNTIME = "unknown_runtime"
    GOLANG = "golang"
    PYTHON = "python"
    PYTHON3 = "python3"
    NODE8 = "node8"
    NODE10 = "node10"
    NODE14 = "node14"
    NODE16 = "node16"
    NODE17 = "node17"
    PYTHON37 = "python37"
    PYTHON38 = "python38"
    PYTHON39 = "python39"
    PYTHON310 = "python310"
    GO113 = "go113"
    GO117 = "go117"
    GO118 = "go118"
    NODE18 = "node18"
    RUST165 = "rust165"
    GO119 = "go119"
    PYTHON311 = "python311"
    PHP82 = "php82"
    NODE19 = "node19"
    GO120 = "go120"

    def __str__(self) -> str:
        return str(self.value)


class FunctionStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"
    CREATED = "created"

    def __str__(self) -> str:
        return str(self.value)


class ListCronsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListDomainsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    HOSTNAME_ASC = "hostname_asc"
    HOSTNAME_DESC = "hostname_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListFunctionsRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListLogsRequestOrderBy(str, Enum):
    TIMESTAMP_DESC = "timestamp_desc"
    TIMESTAMP_ASC = "timestamp_asc"

    def __str__(self) -> str:
        return str(self.value)


class ListNamespacesRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTokensRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class ListTriggersRequestOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)


class LogStream(str, Enum):
    UNKNOWN = "unknown"
    STDOUT = "stdout"
    STDERR = "stderr"

    def __str__(self) -> str:
        return str(self.value)


class NamespaceStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    LOCKED = "locked"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class NullValue(str, Enum):
    NULL_VALUE = "NULL_VALUE"

    def __str__(self) -> str:
        return str(self.value)


class RuntimeStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    BETA = "beta"
    AVAILABLE = "available"
    DEPRECATED = "deprecated"
    END_OF_SUPPORT = "end_of_support"
    END_OF_LIFE = "end_of_life"

    def __str__(self) -> str:
        return str(self.value)


class TokenStatus(str, Enum):
    UNKNOWN = "unknown"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"

    def __str__(self) -> str:
        return str(self.value)


class TriggerInputType(str, Enum):
    UNKNOWN_INPUT_TYPE = "unknown_input_type"
    SQS = "sqs"
    SCW_SQS = "scw_sqs"
    NATS = "nats"
    SCW_NATS = "scw_nats"

    def __str__(self) -> str:
        return str(self.value)


class TriggerStatus(str, Enum):
    UNKNOWN_STATUS = "unknown_status"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    CREATING = "creating"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class CreateTriggerRequestMnqNatsClientConfig:
    mnq_namespace_id: str

    subject: str

    mnq_project_id: str

    mnq_region: str


@dataclass
class CreateTriggerRequestMnqSqsClientConfig:
    mnq_namespace_id: str

    queue: str

    mnq_project_id: str

    mnq_region: str


@dataclass
class CreateTriggerRequestSqsClientConfig:
    endpoint: str

    queue_url: str

    access_key: str

    secret_key: str


@dataclass
class Cron:
    """
    Cron.
    """

    id: str

    function_id: str

    schedule: str

    args: Optional[Dict[str, Any]]

    status: CronStatus

    name: str


@dataclass
class Domain:
    """
    Domain.
    """

    id: str

    hostname: str

    function_id: str

    url: str

    status: DomainStatus

    error_message: Optional[str]


@dataclass
class DownloadURL:
    url: str

    headers: Dict[str, List[str]]


@dataclass
class Function:
    """
    Function.
    """

    id: str

    name: str

    namespace_id: str

    status: FunctionStatus

    environment_variables: Dict[str, str]

    min_scale: int

    max_scale: int

    runtime: FunctionRuntime

    memory_limit: int

    cpu_limit: int

    timeout: Optional[str]

    handler: str

    error_message: Optional[str]

    privacy: FunctionPrivacy

    description: Optional[str]

    domain_name: str

    secret_environment_variables: List[SecretHashedValue]

    region: Region

    http_option: FunctionHttpOption
    """
    Configure how HTTP and HTTPS requests are handled.
    Possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    """

    runtime_message: str


@dataclass
class ListCronsResponse:
    """
    List crons response.
    """

    crons: List[Cron]

    total_count: int


@dataclass
class ListDomainsResponse:
    """
    List domains response.
    """

    domains: List[Domain]

    total_count: int


@dataclass
class ListFunctionRuntimesResponse:
    """
    List function runtimes response.
    """

    runtimes: List[Runtime]

    total_count: int


@dataclass
class ListFunctionsResponse:
    """
    List functions response.
    """

    functions: List[Function]

    total_count: int


@dataclass
class ListLogsResponse:
    """
    List logs response.
    """

    logs: List[Log]

    total_count: int


@dataclass
class ListNamespacesResponse:
    """
    List namespaces response.
    """

    namespaces: List[Namespace]

    total_count: int


@dataclass
class ListTokensResponse:
    tokens: List[Token]

    total_count: int


@dataclass
class ListTriggersResponse:
    triggers: List[Trigger]

    total_count: int


@dataclass
class Log:
    """
    Log.
    """

    message: str

    timestamp: Optional[datetime]

    id: str

    level: str
    """
    Contains the severity of the log (info, debug, error, ...).
    """

    source: str
    """
    Source of the log (core runtime or user code).
    """

    stream: LogStream
    """
    Can be stdout or stderr.
    """


@dataclass
class Namespace:
    """
    Namespace.
    """

    id: str

    name: str

    environment_variables: Dict[str, str]

    organization_id: str

    project_id: str

    status: NamespaceStatus

    registry_namespace_id: str

    error_message: Optional[str]

    registry_endpoint: str

    description: Optional[str]

    secret_environment_variables: List[SecretHashedValue]

    region: Region


@dataclass
class Runtime:
    name: str

    language: str

    version: str

    default_handler: str

    code_sample: str

    status: RuntimeStatus

    status_message: str

    extension: str

    implementation: str


@dataclass
class Secret:
    key: str

    value: Optional[str]


@dataclass
class SecretHashedValue:
    key: str

    hashed_value: str


@dataclass
class Token:
    """
    Token.
    """

    id: str

    token: str

    function_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
    """

    public_key: Optional[str]
    """
    :deprecated
    """

    status: TokenStatus

    description: Optional[str]

    expires_at: Optional[datetime]


@dataclass
class Trigger:
    id: str

    name: str

    description: str

    input_type: TriggerInputType

    status: TriggerStatus

    error_message: Optional[str]

    function_id: str

    scw_sqs_config: Optional[TriggerMnqSqsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """

    sqs_config: Optional[TriggerSqsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """

    scw_nats_config: Optional[TriggerMnqNatsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """


@dataclass
class TriggerMnqNatsClientConfig:
    mnq_namespace_id: str

    subject: str

    mnq_project_id: str

    mnq_region: str


@dataclass
class TriggerMnqSqsClientConfig:
    mnq_namespace_id: str

    queue: str

    mnq_project_id: str

    mnq_region: str


@dataclass
class TriggerSqsClientConfig:
    endpoint: str

    queue_url: str

    access_key: str

    secret_key: str


@dataclass
class UpdateTriggerRequestMnqNatsClientConfig:
    mnq_namespace_id: str

    subject: str

    mnq_project_id: str

    mnq_region: str


@dataclass
class UpdateTriggerRequestMnqSqsClientConfig:
    mnq_namespace_id: str

    queue: str

    mnq_project_id: str

    mnq_region: str


@dataclass
class UpdateTriggerRequestSqsClientConfig:
    endpoint: str

    queue_url: str

    access_key: str

    secret_key: str


@dataclass
class UploadURL:
    """
    Upload url.
    """

    url: str

    headers: Dict[str, List[str]]


@dataclass
class ListNamespacesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListNamespacesRequestOrderBy]

    name: Optional[str]

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class GetNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str


@dataclass
class CreateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]

    environment_variables: Optional[Dict[str, str]]

    project_id: Optional[str]

    description: Optional[str]

    secret_environment_variables: Optional[List[Secret]]


@dataclass
class UpdateNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str

    environment_variables: Optional[Dict[str, str]]

    description: Optional[str]

    secret_environment_variables: Optional[List[Secret]]


@dataclass
class DeleteNamespaceRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    namespace_id: str


@dataclass
class ListFunctionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListFunctionsRequestOrderBy]

    namespace_id: str

    name: Optional[str]

    organization_id: Optional[str]

    project_id: Optional[str]


@dataclass
class GetFunctionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str


@dataclass
class CreateFunctionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]

    namespace_id: str

    environment_variables: Optional[Dict[str, str]]

    min_scale: Optional[int]

    max_scale: Optional[int]

    runtime: FunctionRuntime

    memory_limit: Optional[int]

    timeout: Optional[str]

    handler: Optional[str]

    privacy: FunctionPrivacy

    description: Optional[str]

    secret_environment_variables: Optional[List[Secret]]

    http_option: FunctionHttpOption
    """
    Configure how HTTP and HTTPS requests are handled.
    Possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class UpdateFunctionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str

    environment_variables: Optional[Dict[str, str]]

    min_scale: Optional[int]

    max_scale: Optional[int]

    runtime: FunctionRuntime

    memory_limit: Optional[int]

    timeout: Optional[str]

    redeploy: Optional[bool]

    handler: Optional[str]

    privacy: FunctionPrivacy

    description: Optional[str]

    secret_environment_variables: Optional[List[Secret]]

    http_option: FunctionHttpOption
    """
    Configure how HTTP and HTTPS requests are handled.
    Possible values:
     - redirected: Responds to HTTP request with a 301 redirect to ask the clients to use HTTPS.
     - enabled: Serve both HTTP and HTTPS traffic.
    """


@dataclass
class DeleteFunctionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str


@dataclass
class DeployFunctionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str


@dataclass
class ListFunctionRuntimesRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """


@dataclass
class GetFunctionUploadURLRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str

    content_length: int


@dataclass
class GetFunctionDownloadURLRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str


@dataclass
class ListCronsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListCronsRequestOrderBy]

    function_id: str


@dataclass
class GetCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cron_id: str


@dataclass
class CreateCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str

    schedule: str

    args: Optional[Dict[str, Any]]

    name: Optional[str]


@dataclass
class UpdateCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cron_id: str

    function_id: Optional[str]

    schedule: Optional[str]

    args: Optional[Dict[str, Any]]

    name: Optional[str]


@dataclass
class DeleteCronRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    cron_id: str


@dataclass
class ListLogsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: str

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListLogsRequestOrderBy]


@dataclass
class ListDomainsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListDomainsRequestOrderBy]

    function_id: str


@dataclass
class GetDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    domain_id: str


@dataclass
class CreateDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    hostname: str

    function_id: str


@dataclass
class DeleteDomainRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    domain_id: str


@dataclass
class IssueJWTRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
    """

    expires_at: Optional[datetime]


@dataclass
class CreateTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    function_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id' could be set.
    """

    description: Optional[str]

    expires_at: Optional[datetime]


@dataclass
class GetTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    token_id: str


@dataclass
class ListTokensRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListTokensRequestOrderBy]

    function_id: Optional[str]

    namespace_id: Optional[str]


@dataclass
class DeleteTokenRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    token_id: str


@dataclass
class CreateTriggerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: str

    description: str

    function_id: str

    scw_sqs_config: Optional[CreateTriggerRequestMnqSqsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """

    sqs_config: Optional[CreateTriggerRequestSqsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """

    scw_nats_config: Optional[CreateTriggerRequestMnqNatsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """


@dataclass
class GetTriggerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    trigger_id: str


@dataclass
class ListTriggersRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListTriggersRequestOrderBy]

    function_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
    """

    namespace_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
    """

    project_id: Optional[str]
    """
    One-of ('scope'): at most one of 'function_id', 'namespace_id', 'project_id' could be set.
    """


@dataclass
class UpdateTriggerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    trigger_id: str

    name: Optional[str]

    description: Optional[str]

    scw_sqs_config: Optional[UpdateTriggerRequestMnqSqsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """

    sqs_config: Optional[UpdateTriggerRequestSqsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """

    scw_nats_config: Optional[UpdateTriggerRequestMnqNatsClientConfig]
    """
    One-of ('config'): at most one of 'scw_sqs_config', 'sqs_config', 'scw_nats_config' could be set.
    """


@dataclass
class DeleteTriggerRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    trigger_id: str
