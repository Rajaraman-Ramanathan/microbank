"""
Application configuration.

Reads configuration from Lambda environment variables
and validates values during startup.
"""

import os

from common.execution import ExecutionMode
from common.exceptions import ConfigurationError


class Settings:
    """Application settings."""

    VALID_LOG_LEVELS = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
    }

    def __init__(self) -> None:

        self.mode: ExecutionMode = self._execution_mode()

        self.aws_region: str = os.getenv(
            "AWS_REGION",
            "ap-south-1"
        )

        self.retention_days: int = self._retention_days()

        self.log_level: str = self._log_level()

        self.protected_tags: list[str] = self._csv(
            "PROTECTED_TAGS",
            "DoNotDelete,Retain"
        )

        self.protected_environments: list[str] = self._csv(
            "PROTECTED_ENVIRONMENTS",
            "Production"
        )

    @staticmethod
    def _execution_mode() -> ExecutionMode:
        """
        Validate execution mode.
        """

        mode = os.getenv(
            "MODE",
            "PLAN"
        ).upper()

        try:
            return ExecutionMode(mode)

        except ValueError as ex:
            raise ConfigurationError(
                f"Invalid execution mode '{mode}'. "
                f"Supported values: {ExecutionMode.values()}"
            ) from ex

    @staticmethod
    def _retention_days() -> int:
        """
        Validate retention period.
        """

        value = os.getenv(
            "RETENTION_DAYS",
            "14"
        )

        try:
            retention = int(value)

        except ValueError as ex:
            raise ConfigurationError(
                f"RETENTION_DAYS must be an integer. "
                f"Received '{value}'."
            ) from ex

        if retention <= 0:
            raise ConfigurationError(
                "RETENTION_DAYS must be greater than zero."
            )

        return retention

    @classmethod
    def _log_level(cls) -> str:
        """
        Validate log level.
        """

        level = os.getenv(
            "LOG_LEVEL",
            "INFO"
        ).upper()

        if level not in cls.VALID_LOG_LEVELS:
            raise ConfigurationError(
                f"Invalid LOG_LEVEL '{level}'. "
                f"Supported values: "
                f"{', '.join(sorted(cls.VALID_LOG_LEVELS))}"
            )

        return level

    @staticmethod
    def _csv(name: str, default: str) -> list[str]:
        """
        Convert comma-separated environment variables
        into a list.
        """

        value = os.getenv(name, default)

        return [
            item.strip()
            for item in value.split(",")
            if item.strip()
        ]


settings = Settings()