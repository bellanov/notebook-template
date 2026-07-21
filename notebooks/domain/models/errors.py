"""Errors Models."""

class RetryError(Exception):
    """Base class for retry-related errors."""

class MaxAttemptsExceededError(RetryError):
    """Raised when retry attempts are exhausted."""