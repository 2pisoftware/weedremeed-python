from enum import Enum


class CollectionType(str, Enum):
    BOUNDING_BOX = "Bounding Box"
    BOUNDING_BOX_ORTHOMOSAIC = "Bounding Box Orthomosaic"
    COLOUR_PICKER_OUTPUT = "Colour Picker Output"
    COMPOSITE = "Composite"
    EMPTY = "Empty"
    GEOJSON = "GeoJSON"
    PREPROCESSED = "Preprocessed"
    SWATCH = "Swatch"
    UPLOAD = "Upload"

    def __str__(self) -> str:
        return str(self.value)
