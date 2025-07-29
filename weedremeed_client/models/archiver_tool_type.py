from enum import Enum


class ArchiverToolType(str, Enum):
    ZIP = "ZIP"

    def __str__(self) -> str:
        return str(self.value)
