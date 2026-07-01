from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_status import WorkflowStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_node import WorkflowNode


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """Weedremeed workflow

    Attributes:
        title (str):
        status (WorkflowStatus): The status of a workflow
        input_collection_id (str):
        creator_id (str):
        nodes (list[WorkflowNode]):
        id (str):
        output_collection_id (str | Unset):
    """

    title: str
    status: WorkflowStatus
    input_collection_id: str
    creator_id: str
    nodes: list[WorkflowNode]
    id: str
    output_collection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status = self.status.value

        input_collection_id = self.input_collection_id

        creator_id = self.creator_id

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        id = self.id

        output_collection_id = self.output_collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "status": status,
                "input_collection_id": input_collection_id,
                "creator_id": creator_id,
                "nodes": nodes,
                "id": id,
            }
        )
        if output_collection_id is not UNSET:
            field_dict["output_collection_id"] = output_collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_node import WorkflowNode

        d = dict(src_dict)
        title = d.pop("title")

        status = WorkflowStatus(d.pop("status"))

        input_collection_id = d.pop("input_collection_id")

        creator_id = d.pop("creator_id")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = WorkflowNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        id = d.pop("id")

        output_collection_id = d.pop("output_collection_id", UNSET)

        workflow = cls(
            title=title,
            status=status,
            input_collection_id=input_collection_id,
            creator_id=creator_id,
            nodes=nodes,
            id=id,
            output_collection_id=output_collection_id,
        )

        workflow.additional_properties = d
        return workflow

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
