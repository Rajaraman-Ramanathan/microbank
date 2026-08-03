"""
EKS client wrapper.
"""

from botocore.exceptions import ClientError

from common.aws.base_client import AWSBaseClient
from common.exceptions import AWSOperationError


class EKSClient(AWSBaseClient):

    SERVICE_NAME = "eks"

    def describe_cluster(
        self,
        cluster_name: str
    ) -> dict:
        """
        Returns cluster details.
        """
        try:
            response = self.client.describe_cluster(
                name=cluster_name
            )
            return response["cluster"]

        except ClientError as ex:
            raise AWSOperationError(
                f"Unable to describe cluster "
                f"'{cluster_name}'."
            ) from ex