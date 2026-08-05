class VibraaException(Exception):
    """Base exception for the Vibraa application."""

    def __init__(
        self,
        message: str,
        status_code: int = 400,
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class DatabaseException(VibraaException):
    """Raised when a database operation fails."""

    def __init__(
        self,
        message: str = "Database operation failed",
    ):
        super().__init__(
            message=message,
            status_code=500,
        )