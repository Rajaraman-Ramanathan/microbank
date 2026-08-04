"""
Domain models for the EBS cleanup automation.

These models represent business entities and should not
contain any AWS SDK specific logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from common.execution import ResourceAction


@dataclass(slots=True)
class EBSVolume:
    """
    Domain model representing an EBS volume.
    """

    volume_id: str

    state: str

    size_gib: int

    availability_zone: str

    created_at: datetime

    tags: dict[str, str]


@dataclass(slots=True)
class ResourceEvaluation:
    """
    Represents the evaluation outcome
    for a resource.
    """

    resource: EBSVolume

    action: ResourceAction

    reason: str

@dataclass(slots=True)
class CleanupSummary:

    scanned: int = 0

    deleted: int = 0

    skipped: int = 0

    failed: int = 0