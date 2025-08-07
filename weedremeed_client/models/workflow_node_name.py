from enum import Enum


class WorkflowNodeName(str, Enum):
    WEEDREMEEDCOPIERTOOL = "WeedremeedCopierTool"
    WEEDREMEEDTOOLARCHIVER = "WeedremeedToolArchiver"
    WEEDREMEEDTOOLBINDCOLLECTION = "WeedremeedToolBindCollection"
    WEEDREMEEDTOOLCOLOURPICKERAWS = "WeedremeedToolColourPickerAWS"
    WEEDREMEEDTOOLEXIFREADERAWS = "WeedremeedToolExifReaderAWS"
    WEEDREMEEDTOOLGEOJSONAWS = "WeedremeedToolGeoJsonAWS"
    WEEDREMEEDTOOLPRESETPICKERAWS = "WeedremeedToolPresetPickerAWS"
    WEEDREMEEDTOOLRANDOMSAMPLERAWS = "WeedremeedToolRandomSamplerAWS"
    WEEDREMEEDTOOLYOLOV5AWS = "WeedremeedToolYOLOv5AWS"

    def __str__(self) -> str:
        return str(self.value)
