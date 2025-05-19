from enum import Enum


class RefreshYourApiTokenLoginUnauthorisedError(str, Enum):
    INVALID_TOKEN = "Invalid Token"

    def __str__(self) -> str:
        return str(self.value)
