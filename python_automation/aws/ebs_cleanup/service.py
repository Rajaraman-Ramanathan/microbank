"""
Business logic for orphaned EBS volume cleanup.
"""

from __future__ import annotations

from aws.ebs_cleanup.models import (
    EBSVolume,
    ResourceEvaluation,
    CleanupSummary,
)

from common.aws import EC2Client
from common.config import settings
from common.execution import (
    ExecutionMode,
    ResourceAction,
)
from common.logging import get_logger


logger = get_logger(__name__)


class EBSCleanupService:
    """
    Enterprise service responsible for identifying and
    cleaning orphaned EBS volumes.
    """

    def __init__(self) -> None:

        self.ec2_client = EC2Client()

        self.settings = settings

        self.summary = CleanupSummary()

    def run(self) -> None:
        """
        Main execution workflow.
        """

        logger.info(
            "Starting EBS cleanup automation. Mode=%s",
            self.settings.mode.value,
        )

        logger.info("Automation completed.")

    def discover_resources(self):
        """
        Discover EBS volumes from AWS.

        Returns:
            AWS paginator.
        """
        return self.ec2_client.describe_volumes()

    def map_resource(self, aws_volume: dict) -> EBSVolume:
        """
        Convert an AWS response into a domain model.
        """
        raise NotImplementedError

    def evaluate(
        self,
        volume: EBSVolume,
    ) -> ResourceEvaluation:
        """
        Evaluate a volume against business rules.
        """
        raise NotImplementedError

    def execute(
        self,
        evaluation: ResourceEvaluation,
    ) -> None:
        """
        Execute the evaluated action.
        """
        raise NotImplementedError

    def print_summary(self) -> None:
        """
        Print execution summary.
        """
        raise NotImplementedError