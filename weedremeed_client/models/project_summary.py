from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectSummary")


@_attrs_define
class ProjectSummary:
    """A Weedremeed Project. Groups Collections

    Attributes:
        title (str):
        description (str):
        dt_created (str):
        swatch_collection_id (str): The ID of the collection that holds swatches used for colour picker tools in
            workflows.
        id (str):
        project_group_id (str):
    """

    title: str
    description: str
    dt_created: str
    swatch_collection_id: str
    id: str
    project_group_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        dt_created = self.dt_created

        swatch_collection_id = self.swatch_collection_id

        id = self.id

        project_group_id = self.project_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "description": description,
                "dt_created": dt_created,
                "swatch_collection_id": swatch_collection_id,
                "id": id,
                "project_group_id": project_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description")

        dt_created = d.pop("dt_created")

        swatch_collection_id = d.pop("swatch_collection_id")

        id = d.pop("id")

        project_group_id = d.pop("project_group_id")

        project_summary = cls(
            title=title,
            description=description,
            dt_created=dt_created,
            swatch_collection_id=swatch_collection_id,
            id=id,
            project_group_id=project_group_id,
        )

        project_summary.additional_properties = d
        return project_summary

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
