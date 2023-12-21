# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from scaleway_core.bridge import (
    Region,
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
class JobDefinition:
    id: str

    name: str

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    cpu_limit: int

    memory_limit: int

    image_uri: str

    command: str

    project_id: str

    environment_variables: Dict[str, str]

    description: str

    job_timeout: Optional[str]

    region: Region


@dataclass
class JobRun:
    id: str

    job_definition_id: str

    state: JobRunState

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    terminated_at: Optional[datetime]

    exit_code: Optional[int]

    run_duration: Optional[str]

    error_message: str

    cpu_limit: int

    memory_limit: int

    region: Region


@dataclass
class ListJobDefinitionsResponse:
    job_definitions: List[JobDefinition]

    total_count: int


@dataclass
class ListJobRunsResponse:
    job_runs: List[JobRun]

    total_count: int


@dataclass
class CreateJobDefinitionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    name: Optional[str]
    """
    Name of the job definition.
    """

    cpu_limit: int
    """
    CPU limit of the job.
    """

    memory_limit: int
    """
    Memory limit of the job.
    """

    image_uri: str
    """
    Image to use for the job.
    """

    command: str
    """
    Startup command.
    """

    project_id: Optional[str]
    """
    UUID of the Scaleway Project containing the job.
    """

    environment_variables: Optional[Dict[str, str]]
    """
    Environment variables of the job.
    """

    description: str
    """
    Description of the job.
    """

    job_timeout: Optional[str]
    """
    Timeout of the job in seconds.
    """


@dataclass
class GetJobDefinitionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_definition_id: str
    """
    UUID of the job definition to get.
    """


@dataclass
class ListJobDefinitionsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListJobDefinitionsRequestOrderBy]

    project_id: Optional[str]


@dataclass
class UpdateJobDefinitionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_definition_id: str
    """
    UUID of the job definition to update.
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
    Memory limit of the job.
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


@dataclass
class DeleteJobDefinitionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_definition_id: str
    """
    UUID of the job definition to delete.
    """


@dataclass
class StartJobDefinitionRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_definition_id: str
    """
    UUID of the job definition to start.
    """


@dataclass
class GetJobRunRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_run_id: str
    """
    UUID of the job run to get.
    """


@dataclass
class StopJobRunRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    job_run_id: str
    """
    UUID of the job run to stop.
    """


@dataclass
class ListJobRunsRequest:
    region: Optional[Region]
    """
    Region to target. If none is passed will use default region from the config.
    """

    page: Optional[int]

    page_size: Optional[int]

    order_by: Optional[ListJobRunsRequestOrderBy]

    job_definition_id: Optional[str]

    project_id: Optional[str]
