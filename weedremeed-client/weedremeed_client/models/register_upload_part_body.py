from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegisterUploadPartBody")


@_attrs_define
class RegisterUploadPartBody:
    """
    Attributes:
        id (str): The upload ID provided by /weedremeed-api/upload
        part (str): The part number of this part
        length (int): The content-length of this part
        md5 (str): The md5 hash of this part
    """

    id: str
    part: str
    length: int
    md5: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        part = self.part

        length = self.length

        md5 = self.md5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "part": part,
                "length": length,
                "md5": md5,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        part = d.pop("part")

        length = d.pop("length")

        md5 = d.pop("md5")

        register_upload_part_body = cls(
            id=id,
            part=part,
            length=length,
            md5=md5,
        )

        register_upload_part_body.additional_properties = d
        return register_upload_part_body

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
