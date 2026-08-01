"""
Application configuration.

Reads configuration from Lambda environment variables
and validates values during startup.
"""

import os

from common.execution import ExecutionMode


class Settings:
    """Application settings."""

    def __init__(self):

        self.mode = self._execution_mode()

        self.aws_region = os.getenv(
            "AWS_REGION",
            "ap-south-1"
        )

        self.retention_days = int(
            os.getenv("RETENTION_DAYS", "14")
        )

        self.log_level = os.getenv(
            "LOG_LEVEL",
            "INFO"
        ).upper()

        self.protected_tags = self._csv(
            "PROTECTED_TAGS",
            "DoNotDelete,Retain"
        )

        self.protected_environments = self._csv(
            "PROTECTED_ENVIRONMENTS",
            "Production"
        )

    @staticmethod
    def _csv(name: str, default: str) -> list[str]:
        """
        Convert comma separated environment variables
        into a list.
        """
        value = os.getenv(name, default)

        return [
            item.strip()
            for item in value.split(",")
            if item.strip()
        ]

    @staticmethod
    def _execution_mode() -> ExecutionMode:
        """
        Validate execution mode.
        """

        mode = os.getenv(
            "MODE",
            "PLAN"
        ).upper()

        return ExecutionMode(mode)

settings = Settings()