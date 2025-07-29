from enum import Enum


class CollectionStatus(str, Enum):
    BUSY = "Busy"
    DRAFT = "Draft"
    READY = "Ready"

    def __str__(self) -> str:
        return str(self.value)
