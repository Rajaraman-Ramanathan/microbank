"""
CloudWatch client wrapper.
"""

from botocore.exceptions import ClientError

from common.aws.base_client import AWSBaseClient
from common.exceptions import AWSOperationError


class CloudWatchClient(AWSBaseClient):

    SERVICE_NAME = "cloudwatch"

    def put_metric(
        self,
        namespace: str,
        metric_name: str,
        value: float,
        unit: str = "Count"
    ) -> None:
        """
        Publishes a custom CloudWatch metric.
        """
        try:
            self.client.put_metric_data(
                Namespace=namespace,
                MetricData=[
                    {
                        "MetricName": metric_name,
                        "Value": value,
                        "Unit": unit,
                    }
                ]
            )

        except ClientError as ex:
            raise AWSOperationError(
                "Unable to publish CloudWatch metric."
            ) from ex