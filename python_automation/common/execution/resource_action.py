"""
Defines the actions an automation may take
for an individual resource.
"""

from enum import Enum


class ResourceAction(str, Enum):
    """Supported resource actions."""

    DELETE = "DELETE"
    SKIP = "SKIP"
    REPORT = "REPORT"

    @classmethod
    def values(cls) -> list[str]:
        return [action.value for action in cls]