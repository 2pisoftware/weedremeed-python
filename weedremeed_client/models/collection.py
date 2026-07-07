from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_status import CollectionStatus
from ..models.collection_type import CollectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_metadata import CollectionMetadata


T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """A Weedremeed Collection containing various files.

    Attributes:
        title (str):
        type_ (CollectionType): Weedremeed Collection Type Default: CollectionType.EMPTY.
        status (CollectionStatus): Collection Processing Status
        creator_id (str):
        dt_created (str): ISO8601
        size (int):
        id (str):
        project_id (str):
        description (str | Unset):
        metadata (CollectionMetadata | Unset):
        dt_modified (str | Unset): ISO8601
    """

    title: str
    status: CollectionStatus
    creator_id: str
    dt_created: str
    size: int
    id: str
    project_id: str
    type_: CollectionType = CollectionType.EMPTY
    description: str | Unset = UNSET
    metadata: CollectionMetadata | Unset = UNSET
    dt_modified: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_.value

        status = self.status.value

        creator_id = self.creator_id

        dt_created = self.dt_created

        size = self.size

        id = self.id

        project_id = self.project_id

        description = self.description

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        dt_modified = self.dt_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "type": type_,
                "status": status,
                "creator_id": creator_id,
                "dt_created": dt_created,
                "size": size,
                "id": id,
                "project_id": project_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if dt_modified is not UNSET:
            field_dict["dt_modified"] = dt_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_metadata import CollectionMetadata

        d = dict(src_dict)
        title = d.pop("title")

        type_ = CollectionType(d.pop("type"))

        status = CollectionStatus(d.pop("status"))

        creator_id = d.pop("creator_id")

        dt_created = d.pop("dt_created")

        size = d.pop("size")

        id = d.pop("id")

        project_id = d.pop("project_id")

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CollectionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CollectionMetadata.from_dict(_metadata)

        dt_modified = d.pop("dt_modified", UNSET)

        collection = cls(
            title=title,
            type_=type_,
            status=status,
            creator_id=creator_id,
            dt_created=dt_created,
            size=size,
            id=id,
            project_id=project_id,
            description=description,
            metadata=metadata,
            dt_modified=dt_modified,
        )

        collection.additional_properties = d
        return collection

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
