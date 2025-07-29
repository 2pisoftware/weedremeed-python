from enum import Enum


class ColourPickerToolColourSpace(str, Enum):
    HSV = "HSV"
    RGB = "RGB"

    def __str__(self) -> str:
        return str(self.value)
