"""
Base AWS client.

Provides a reusable boto3 session for all AWS service wrappers.
"""

from __future__ import annotations

from abc import ABC
from typing import Any

import boto3

from common.config import settings


class AWSBaseClient(ABC):
    """
    Base class for all AWS service clients.

    Responsibilities:
        - Create a shared boto3 session.
        - Initialize the AWS service client.
        - Expose the underlying boto3 client when required.

    Business logic must never exist in this class.
    """

    SERVICE_NAME: str | None = None

    # Shared boto3 session reused by every AWS client
    _session: boto3.Session | None = None

    def __init__(self) -> None:
        if not self.SERVICE_NAME:
            raise NotImplementedError(
                f"{self.__class__.__name__} must define SERVICE_NAME."
            )

        if AWSBaseClient._session is None:
            AWSBaseClient._session = boto3.Session(
                region_name=settings.aws_region
            )

        self.session: boto3.Session = AWSBaseClient._session
        self.client: Any = self.session.client(
            self.SERVICE_NAME
        )

    def get_client(self) -> Any:
        """
        Returns the underlying boto3 client.

        This should only be used for advanced operations
        that are not yet wrapped by this framework.
        """
        return self.client