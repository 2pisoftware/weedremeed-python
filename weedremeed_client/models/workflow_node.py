from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_node_name import WorkflowNodeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archiver_tool import ArchiverTool
    from ..models.collection_bind_tool import CollectionBindTool
    from ..models.colour_picker_tool import ColourPickerTool
    from ..models.geo_json_tool import GeoJsonTool
    from ..models.preset_picker_tool import PresetPickerTool
    from ..models.random_sampler_tool import RandomSamplerTool
    from ..models.yol_ov_5_tool import YOLOv5Tool


T = TypeVar("T", bound="WorkflowNode")


@_attrs_define
class WorkflowNode:
    """A node within a workflow. In the UI, this is a 'tool'

    Attributes:
        config (Union['ArchiverTool', 'CollectionBindTool', 'ColourPickerTool', 'GeoJsonTool', 'PresetPickerTool',
            'RandomSamplerTool', 'YOLOv5Tool', None]):
        export (bool): When true, this node will export it's output to a separate collection in addition to the normal
            workflow output collection.
        name (WorkflowNodeName):
        output_collection_id (Union[Unset, str]): Null when output is not ready yet, or `export` is false.
    """

    config: Union[
        "ArchiverTool",
        "CollectionBindTool",
        "ColourPickerTool",
        "GeoJsonTool",
        "PresetPickerTool",
        "RandomSamplerTool",
        "YOLOv5Tool",
        None,
    ]
    export: bool
    name: WorkflowNodeName
    output_collection_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.archiver_tool import ArchiverTool
        from ..models.collection_bind_tool import CollectionBindTool
        from ..models.colour_picker_tool import ColourPickerTool
        from ..models.geo_json_tool import GeoJsonTool
        from ..models.preset_picker_tool import PresetPickerTool
        from ..models.random_sampler_tool import RandomSamplerTool
        from ..models.yol_ov_5_tool import YOLOv5Tool

        config: Union[None, dict[str, Any]]
        if isinstance(self.config, ColourPickerTool):
            config = self.config.to_dict()
        elif isinstance(self.config, ArchiverTool):
            config = self.config.to_dict()
        elif isinstance(self.config, GeoJsonTool):
            config = self.config.to_dict()
        elif isinstance(self.config, RandomSamplerTool):
            config = self.config.to_dict()
        elif isinstance(self.config, CollectionBindTool):
            config = self.config.to_dict()
        elif isinstance(self.config, PresetPickerTool):
            config = self.config.to_dict()
        elif isinstance(self.config, YOLOv5Tool):
            config = self.config.to_dict()
        else:
            config = self.config

        export = self.export

        name = self.name.value

        output_collection_id = self.output_collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "export": export,
                "name": name,
            }
        )
        if output_collection_id is not UNSET:
            field_dict["output_collection_id"] = output_collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.archiver_tool import ArchiverTool
        from ..models.collection_bind_tool import CollectionBindTool
        from ..models.colour_picker_tool import ColourPickerTool
        from ..models.geo_json_tool import GeoJsonTool
        from ..models.preset_picker_tool import PresetPickerTool
        from ..models.random_sampler_tool import RandomSamplerTool
        from ..models.yol_ov_5_tool import YOLOv5Tool

        d = dict(src_dict)

        def _parse_config(
            data: object,
        ) -> Union[
            "ArchiverTool",
            "CollectionBindTool",
            "ColourPickerTool",
            "GeoJsonTool",
            "PresetPickerTool",
            "RandomSamplerTool",
            "YOLOv5Tool",
            None,
        ]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ColourPickerTool.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = ArchiverTool.from_dict(data)

                return config_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_3 = GeoJsonTool.from_dict(data)

                return config_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_4 = RandomSamplerTool.from_dict(data)

                return config_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_5 = CollectionBindTool.from_dict(data)

                return config_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_6 = PresetPickerTool.from_dict(data)

                return config_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_7 = YOLOv5Tool.from_dict(data)

                return config_type_7
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "ArchiverTool",
                    "CollectionBindTool",
                    "ColourPickerTool",
                    "GeoJsonTool",
                    "PresetPickerTool",
                    "RandomSamplerTool",
                    "YOLOv5Tool",
                    None,
                ],
                data,
            )

        config = _parse_config(d.pop("config"))

        export = d.pop("export")

        name = WorkflowNodeName(d.pop("name"))

        output_collection_id = d.pop("output_collection_id", UNSET)

        workflow_node = cls(
            config=config,
            export=export,
            name=name,
            output_collection_id=output_collection_id,
        )

        workflow_node.additional_properties = d
        return workflow_node

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
