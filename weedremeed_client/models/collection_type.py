from enum import Enum


class CollectionType(str, Enum):
    ARCHIVE_OUTPUT = "Archive Output"
    BOUNDING_BOX = "Bounding Box"
    BOUNDING_BOX_ORTHOMOSAIC = "Bounding Box Orthomosaic"
    COLOUR_PICKER_OUTPUT = "Colour Picker Output"
    COMPOSITE = "Composite"
    DUPLICATED_UPLOAD = "Duplicated Upload"
    EMPTY = "Empty"
    EXIF_READER_OUTPUT = "Exif Reader Output"
    GEOJSON = "GeoJSON"
    GEOJSON_OUTPUT = "GeoJson Output"
    PREPROCESSED = "Preprocessed"
    REFERENCE_TO_BASE_COLLECTION = "Reference To Base Collection"
    SHARED_COLLECTION_SOURCE = "Shared Collection Source"
    SWATCH = "Swatch"
    UPLOAD = "Upload"
    YOLOV5_MODEL_OUTPUT = "YOLOv5 Model Output"

    def __str__(self) -> str:
        return str(self.value)
