# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.
from typing import List

from .types import (
    BookingStatus,
    JobStatus,
    ProcessStatus,
    SessionStatus,
)

BOOKING_TRANSIENT_STATUSES: List[BookingStatus] = [
    BookingStatus.WAITING,
    BookingStatus.VALIDATING,
    BookingStatus.CANCELLING,
]
"""
Lists transient statutes of the enum :class:`BookingStatus <BookingStatus>`.
"""
JOB_TRANSIENT_STATUSES: List[JobStatus] = [
    JobStatus.WAITING,
    JobStatus.RUNNING,
    JobStatus.CANCELLING,
]
"""
Lists transient statutes of the enum :class:`JobStatus <JobStatus>`.
"""
PROCESS_TRANSIENT_STATUSES: List[ProcessStatus] = [
    ProcessStatus.STARTING,
    ProcessStatus.RUNNING,
    ProcessStatus.CANCELLING,
]
"""
Lists transient statutes of the enum :class:`ProcessStatus <ProcessStatus>`.
"""
SESSION_TRANSIENT_STATUSES: List[SessionStatus] = [
    SessionStatus.STARTING,
    SessionStatus.STOPPING,
]
"""
Lists transient statutes of the enum :class:`SessionStatus <SessionStatus>`.
"""
