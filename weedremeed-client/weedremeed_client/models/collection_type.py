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
    YOLOV5_OUTPUT = "YOLOv5 Model Output"
    EXIF_READER_OUTPUT = "Exif Reader Output"
    GEOJSON_OUTPUT = "GeoJson Output"
    ARCHIVE_OUTPUT = "Archive Output"    
    SHARED_COPY_SOURCE = "Shared Collection Source"
    UPLOAD_DUPLICATE = "Duplicated Upload"
    OPAQUE_REFERENCE = "Reference To Base Collection"


    def __str__(self) -> str:
        return str(self.value)
