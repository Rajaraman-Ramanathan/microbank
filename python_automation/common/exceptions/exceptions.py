"""
Custom exceptions used throughout the automation framework.

These exceptions provide a consistent abstraction over
configuration, validation and cloud provider errors.
"""


class AutomationError(Exception):
    """
    Base exception for the automation framework.

    Every custom exception should inherit from this class.
    """

    pass


class ConfigurationError(AutomationError):
    """
    Raised when the application configuration
    is missing or invalid.
    """

    pass


class ValidationError(AutomationError):
    """
    Raised when business rule validation fails.
    """

    pass


class AWSOperationError(AutomationError):
    """
    Raised when an AWS API operation fails.

    Example:
        DeleteVolume
        ReleaseAddress
        DescribeVolumes
    """

    pass


class KubernetesOperationError(AutomationError):
    """
    Raised when a Kubernetes API operation fails.
    """

    pass


class ResourceNotFoundError(AutomationError):
    """
    Raised when an expected resource
    cannot be found.
    """

    pass