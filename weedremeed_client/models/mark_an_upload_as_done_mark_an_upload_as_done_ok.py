from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mark_an_upload_as_done_mark_an_upload_as_done_ok_data import (
        MarkAnUploadAsDoneMarkAnUploadAsDoneOkData,
    )


T = TypeVar("T", bound="MarkAnUploadAsDoneMarkAnUploadAsDoneOk")


@_attrs_define
class MarkAnUploadAsDoneMarkAnUploadAsDoneOk:
    """
    Attributes:
        status (int):
        success (bool):
        message (str):
        data (MarkAnUploadAsDoneMarkAnUploadAsDoneOkData):
    """

    status: int
    success: bool
    message: str
    data: MarkAnUploadAsDoneMarkAnUploadAsDoneOkData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        success = self.success

        message = self.message

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "success": success,
                "message": message,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mark_an_upload_as_done_mark_an_upload_as_done_ok_data import (
            MarkAnUploadAsDoneMarkAnUploadAsDoneOkData,
        )

        d = dict(src_dict)
        status = d.pop("status")

        success = d.pop("success")

        message = d.pop("message")

        data = MarkAnUploadAsDoneMarkAnUploadAsDoneOkData.from_dict(d.pop("data"))

        mark_an_upload_as_done_mark_an_upload_as_done_ok = cls(
            status=status,
            success=success,
            message=message,
            data=data,
        )

        mark_an_upload_as_done_mark_an_upload_as_done_ok.additional_properties = d
        return mark_an_upload_as_done_mark_an_upload_as_done_ok

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
