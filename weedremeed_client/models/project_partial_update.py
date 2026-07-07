from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectPartialUpdate")


@_attrs_define
class ProjectPartialUpdate:
    """Data transfer object for partially updating an existing Project (PATCH operation).

    Attributes:
        title (str | Unset):
        description (str | Unset):
        swatch_collection_id (str | Unset):
        project_group_id (str | Unset):
    """

    title: str | Unset = UNSET
    description: str | Unset = UNSET
    swatch_collection_id: str | Unset = UNSET
    project_group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        swatch_collection_id = self.swatch_collection_id

        project_group_id = self.project_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if swatch_collection_id is not UNSET:
            field_dict["swatch_collection_id"] = swatch_collection_id
        if project_group_id is not UNSET:
            field_dict["project_group_id"] = project_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        swatch_collection_id = d.pop("swatch_collection_id", UNSET)

        project_group_id = d.pop("project_group_id", UNSET)

        project_partial_update = cls(
            title=title,
            description=description,
            swatch_collection_id=swatch_collection_id,
            project_group_id=project_group_id,
        )

        project_partial_update.additional_properties = d
        return project_partial_update

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
