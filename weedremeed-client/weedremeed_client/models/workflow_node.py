from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_node_config import WorkflowNodeConfig


T = TypeVar("T", bound="WorkflowNode")


@_attrs_define
class WorkflowNode:
    """A node within a workflow. In the UI, this is a 'tool'

    Attributes:
        name (str):
        config (WorkflowNodeConfig):
        export (bool): When true, this node will export it's output to a separate collection in addition to the normal
            workflow output collection.
        output_collection_id (Union[Unset, str]): Null when output is not ready yet, or `export` is false.
    """

    name: str
    config: "WorkflowNodeConfig"
    export: bool
    output_collection_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        config = self.config.to_dict()

        export = self.export

        output_collection_id = self.output_collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "config": config,
                "export": export,
            }
        )
        if output_collection_id is not UNSET:
            field_dict["output_collection_id"] = output_collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_node_config import WorkflowNodeConfig

        d = dict(src_dict)
        name = d.pop("name")

        config = WorkflowNodeConfig.from_dict(d.pop("config"))

        export = d.pop("export")

        output_collection_id = d.pop("output_collection_id", UNSET)

        workflow_node = cls(
            name=name,
            config=config,
            export=export,
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
