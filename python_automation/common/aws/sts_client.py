"""
STS client wrapper.
"""

from botocore.exceptions import ClientError

from common.aws.base_client import AWSBaseClient
from common.exceptions import AWSOperationError


class STSClient(AWSBaseClient):

    SERVICE_NAME = "sts"

    def caller_identity(self) -> dict:
        """
        Returns current AWS caller identity.
        """
        try:
            return self.client.get_caller_identity()

        except ClientError as ex:
            raise AWSOperationError(
                "Unable to retrieve caller identity."
            ) from ex