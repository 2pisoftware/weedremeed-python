from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegisterUploadPartRegisterUploadPartOk")


@_attrs_define
class RegisterUploadPartRegisterUploadPartOk:
    """
    Attributes:
        endpoint (str): A presigned URL to be used to upload this part's data
    """

    endpoint: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        register_upload_part_register_upload_part_ok = cls(
            endpoint=endpoint,
        )

        register_upload_part_register_upload_part_ok.additional_properties = d
        return register_upload_part_register_upload_part_ok

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
