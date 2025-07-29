from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """A Weedremeed Project. Groups Collections

    Attributes:
        title (str):
        dt_created (str):
        collections (list['Collection']):
        id (str):
        project_group_id (str):
        description (Union[Unset, str]):
        swatch_collection_id (Union[Unset, str]): The ID of the collection that holds swatches used for colour picker
            tools in workflows.
    """

    title: str
    dt_created: str
    collections: list["Collection"]
    id: str
    project_group_id: str
    description: Union[Unset, str] = UNSET
    swatch_collection_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        dt_created = self.dt_created

        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        id = self.id

        project_group_id = self.project_group_id

        description = self.description

        swatch_collection_id = self.swatch_collection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "dt_created": dt_created,
                "collections": collections,
                "id": id,
                "project_group_id": project_group_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if swatch_collection_id is not UNSET:
            field_dict["swatch_collection_id"] = swatch_collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection import Collection

        d = dict(src_dict)
        title = d.pop("title")

        dt_created = d.pop("dt_created")

        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = Collection.from_dict(collections_item_data)

            collections.append(collections_item)

        id = d.pop("id")

        project_group_id = d.pop("project_group_id")

        description = d.pop("description", UNSET)

        swatch_collection_id = d.pop("swatch_collection_id", UNSET)

        project = cls(
            title=title,
            dt_created=dt_created,
            collections=collections,
            id=id,
            project_group_id=project_group_id,
            description=description,
            swatch_collection_id=swatch_collection_id,
        )

        project.additional_properties = d
        return project

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
