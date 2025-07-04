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

class JobRunState(str, Enum, metaclass=StrEnumMeta):
    UNKNOWN_STATE = "unknown_state"
    QUEUED = "queued"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"
    INTERNAL_ERROR = "internal_error"

    def __str__(self) -> str:
        return str(self.value)

class ListJobDefinitionsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)

class ListJobRunsRequestOrderBy(str, Enum, metaclass=StrEnumMeta):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"

    def __str__(self) -> str:
        return str(self.value)

@dataclass
class SecretEnvVar:
    name: str
    

@dataclass
class SecretFile:
    path: str
    

@dataclass
class CronSchedule:
    schedule: str
    """
    UNIX cron schedule to run job (e.g., '* * * * *').
    """
    
    timezone: str
    """
    Timezone for the cron schedule, in tz database format (e.g., 'Europe/Paris').
    """
    

@dataclass
class CreateJobDefinitionRequestCronScheduleConfig:
    schedule: str
    
    timezone: str
    

@dataclass
class CreateJobDefinitionSecretsRequestSecretConfig:
    secret_manager_id: str
    
    secret_manager_version: str
    
    path: Optional[str]
    
    env_var_name: Optional[str]
    

@dataclass
class Secret:
    secret_id: str
    """
    UUID of the secret reference within the job.
    """
    
    secret_manager_id: str
    """
    UUID of the secret in Secret Manager.
    """
    
    secret_manager_version: str
    """
    Version of the secret in Secret Manager.
    """
    
    file: Optional[SecretFile]
    
    env_var: Optional[SecretEnvVar]
    

@dataclass
class JobDefinition:
    id: str
    
    name: str
    
    cpu_limit: int
    
    memory_limit: int
    
    image_uri: str
    
    command: str
    
    project_id: str
    
    created_at: Optional[datetime]
    
    updated_at: Optional[datetime]
    
    environment_variables: Dict[str, str]
    
    description: str
    
    local_storage_capacity: int
    
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    job_timeout: Optional[str]
    
    cron_schedule: Optional[CronSchedule]
    

@dataclass
class JobRun:
    id: str
    
    job_definition_id: str
    
    state: JobRunState
    
    error_message: str
    
    cpu_limit: int
    
    memory_limit: int
    
    command: str
    
    created_at: Optional[datetime]
    
    updated_at: Optional[datetime]
    
    terminated_at: Optional[datetime]
    
    exit_code: Optional[int]
    
    run_duration: Optional[str]
    
    environment_variables: Dict[str, str]
    
    local_storage_capacity: int
    
    region: ScwRegion
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    started_at: Optional[datetime]
    

@dataclass
class Resource:
    cpu_limit: int
    
    memory_limit: int
    

@dataclass
class UpdateJobDefinitionRequestCronScheduleConfig:
    schedule: Optional[str]
    
    timezone: Optional[str]
    

@dataclass
class CreateJobDefinitionRequest:
    cpu_limit: int
    """
    CPU limit of the job.
    """
    
    memory_limit: int
    """
    Memory limit of the job (in MiB).
    """
    
    image_uri: str
    """
    Image to use for the job.
    """
    
    command: str
    """
    Startup command. If empty or not defined, the image's default command is used.
    """
    
    description: str
    """
    Description of the job.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    name: Optional[str]
    """
    Name of the job definition.
    """
    
    local_storage_capacity: Optional[int]
    """
    Local storage capacity of the job (in MiB).
    """
    
    project_id: Optional[str]
    """
    UUID of the Scaleway Project containing the job.
    """
    
    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the job.
    """
    
    job_timeout: Optional[str]
    """
    Timeout of the job in seconds.
    """
    
    cron_schedule: Optional[CreateJobDefinitionRequestCronScheduleConfig]
    """
    Configure a cron for the job.
    """
    

@dataclass
class CreateJobDefinitionSecretsRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """
    
    secrets: List[CreateJobDefinitionSecretsRequestSecretConfig]
    """
    List of secrets to inject into the job.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class CreateJobDefinitionSecretsResponse:
    secrets: List[Secret]
    """
    List of secrets created.
    """
    

@dataclass
class DeleteJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to delete.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class DeleteJobDefinitionSecretRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """
    
    secret_id: str
    """
    UUID of the secret reference within the job.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class GetJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to get.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class GetJobDefinitionSecretRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """
    
    secret_id: str
    """
    UUID of the secret reference within the job.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class GetJobRunRequest:
    job_run_id: str
    """
    UUID of the job run to get.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class GetJobsLimitsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class JobsLimits:
    secrets_per_job_definition: int
    

@dataclass
class ListJobDefinitionSecretsRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class ListJobDefinitionSecretsResponse:
    secrets: List[Secret]
    """
    List of secret references within a job definition.
    """
    
    total_count: int
    """
    Total count of secret references within a job definition.
    """
    

@dataclass
class ListJobDefinitionsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    page: Optional[int]
    
    page_size: Optional[int]
    
    order_by: Optional[ListJobDefinitionsRequestOrderBy]
    
    project_id: Optional[str]
    
    organization_id: Optional[str]
    

@dataclass
class ListJobDefinitionsResponse:
    job_definitions: List[JobDefinition]
    
    total_count: int
    

@dataclass
class ListJobRunsRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    page: Optional[int]
    
    page_size: Optional[int]
    
    order_by: Optional[ListJobRunsRequestOrderBy]
    
    job_definition_id: Optional[str]
    
    project_id: Optional[str]
    
    organization_id: Optional[str]
    
    state: Optional[JobRunState]
    
    states: Optional[List[JobRunState]]
    

@dataclass
class ListJobRunsResponse:
    job_runs: List[JobRun]
    
    total_count: int
    

@dataclass
class ListJobsResourcesRequest:
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class ListJobsResourcesResponse:
    resources: List[Resource]
    

@dataclass
class StartJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to start.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    command: Optional[str]
    """
    Contextual startup command for this specific job run.
    """
    
    environment_variables: Optional[Dict[str, str]]
    """
    Contextual environment variables for this specific job run.
    """
    
    replicas: Optional[int]
    """
    Number of jobs to run.
    """
    

@dataclass
class StartJobDefinitionResponse:
    job_runs: List[JobRun]
    

@dataclass
class StopJobRunRequest:
    job_run_id: str
    """
    UUID of the job run to stop.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    

@dataclass
class UpdateJobDefinitionRequest:
    job_definition_id: str
    """
    UUID of the job definition to update.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    name: Optional[str]
    """
    Name of the job definition.
    """
    
    cpu_limit: Optional[int]
    """
    CPU limit of the job.
    """
    
    memory_limit: Optional[int]
    """
    Memory limit of the job (in MiB).
    """
    
    local_storage_capacity: Optional[int]
    """
    Local storage capacity of the job (in MiB).
    """
    
    image_uri: Optional[str]
    """
    Image to use for the job.
    """
    
    command: Optional[str]
    """
    Startup command.
    """
    
    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the job.
    """
    
    description: Optional[str]
    """
    Description of the job.
    """
    
    job_timeout: Optional[str]
    """
    Timeout of the job in seconds.
    """
    
    cron_schedule: Optional[UpdateJobDefinitionRequestCronScheduleConfig]
    

@dataclass
class UpdateJobDefinitionSecretRequest:
    job_definition_id: str
    """
    UUID of the job definition.
    """
    
    secret_id: str
    """
    UUID of the secret reference within the job.
    """
    
    region: Optional[ScwRegion]
    """
    Region to target. If none is passed will use default region from the config.
    """
    
    secret_manager_version: Optional[str]
    """
    Version of the secret in Secret Manager.
    """
    
    path: Optional[str]
    
    env_var_name: Optional[str]
    
