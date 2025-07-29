from enum import Enum


class YOLOv5ToolModel(str, Enum):
    WHEEL_CACTUS = "Wheel Cactus"

    def __str__(self) -> str:
        return str(self.value)
