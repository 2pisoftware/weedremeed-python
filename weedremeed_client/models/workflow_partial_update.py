from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_node import WorkflowNode


T = TypeVar("T", bound="WorkflowPartialUpdate")


@_attrs_define
class WorkflowPartialUpdate:
    """Data transfer object for partially updating an existing Workflow (PATCH operation).

    Attributes:
        title (str | Unset):
        input_collection_id (str | Unset):
        nodes (list[WorkflowNode] | Unset):
    """

    title: str | Unset = UNSET
    input_collection_id: str | Unset = UNSET
    nodes: list[WorkflowNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        input_collection_id = self.input_collection_id

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if input_collection_id is not UNSET:
            field_dict["input_collection_id"] = input_collection_id
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_node import WorkflowNode

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        input_collection_id = d.pop("input_collection_id", UNSET)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[WorkflowNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = WorkflowNode.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        workflow_partial_update = cls(
            title=title,
            input_collection_id=input_collection_id,
            nodes=nodes,
        )

        workflow_partial_update.additional_properties = d
        return workflow_partial_update

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
