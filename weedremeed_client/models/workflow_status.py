from enum import Enum


class WorkflowStatus(str, Enum):
    DONE = "DONE"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NEW = "NEW"

    def __str__(self) -> str:
        return str(self.value)
