"""
EC2 client wrapper.
"""
from typing import Any

from botocore.exceptions import ClientError
from botocore.paginate import PageIterator

from common.aws.base_client import AWSBaseClient
from common.exceptions import AWSOperationError


class EC2Client(AWSBaseClient):

    SERVICE_NAME = "ec2"

    def list_ebs_volumes(self) -> PageIterator:
        """
        Returns paginator for all EBS volumes.
        """
        try:
            return self.client.get_paginator(
                "describe_volumes"
            )

        except ClientError as ex:
            raise AWSOperationError(
                "Unable to retrieve EBS volumes."
            ) from ex

    def delete_ebs_volume(self, volume_id: str) -> None:
        """
        Deletes an EBS volume.
        """
        try:
            self.client.delete_volume(
                VolumeId=volume_id
            )

        except ClientError as ex:
            raise AWSOperationError(
                f"Unable to delete EBS volume "
                f"'{volume_id}'."
            ) from ex

    def describe_addresses(self) -> dict[str, Any]:
        """
        Returns all Elastic IP addresses.
        """

        try:
            return self.client.describe_addresses()

        except ClientError as ex:
            raise AWSOperationError(
                "Failed to describe Elastic IP addresses."
            ) from ex

    def release_address(
        self,
        allocation_id: str
    ) -> None:
        """
        Release an Elastic IP.
        """
        try:
            self.client.release_address(
                AllocationId=allocation_id
            )

        except ClientError as ex:
            raise AWSOperationError(
                f"Failed to release Elastic IP "
                f"'{allocation_id}'."
            ) from ex

    def describe_instances(self) -> PageIterator:
        """
        Returns paginator for EC2 instances.
        """
        try:
            return self.client.get_paginator(
                "describe_instances"
            )

        except ClientError as ex:
            raise AWSOperationError(
                "Failed to describe EC2 instances."
            ) from ex