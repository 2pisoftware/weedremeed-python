from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """A file uploaded to a collection

    Attributes:
        id (str):
        dt_created (str):
        filename (str):
        url (str): A presigned URL to access this attachment. Expires in 1 hour
        dt_modified (Union[Unset, str]):
    """

    id: str
    dt_created: str
    filename: str
    url: str
    dt_modified: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dt_created = self.dt_created

        filename = self.filename

        url = self.url

        dt_modified = self.dt_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dt_created": dt_created,
                "filename": filename,
                "url": url,
            }
        )
        if dt_modified is not UNSET:
            field_dict["dt_modified"] = dt_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        dt_created = d.pop("dt_created")

        filename = d.pop("filename")

        url = d.pop("url")

        dt_modified = d.pop("dt_modified", UNSET)

        attachment = cls(
            id=id,
            dt_created=dt_created,
            filename=filename,
            url=url,
            dt_modified=dt_modified,
        )

        attachment.additional_properties = d
        return attachment

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
