"""
Defines the supported execution modes for automation workflows.

Every automation in this framework should operate in one of these modes.

PLAN     : Discover resources and report actions without making changes.
EXECUTE  : Perform the actual automation.
REPORT   : Generate inventory or compliance reports without evaluating actions.
"""

from enum import Enum


class ExecutionMode(str, Enum):
    """Supported execution modes for automation workflows."""
    PLAN = "PLAN"
    EXECUTE = "EXECUTE"
    REPORT = "REPORT"

    @classmethod
    def values(cls) -> list[str]:
        return [mode.value for mode in cls]