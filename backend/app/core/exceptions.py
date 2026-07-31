class VibraaException(Exception):
    """Base exception for the Vibraa application."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)