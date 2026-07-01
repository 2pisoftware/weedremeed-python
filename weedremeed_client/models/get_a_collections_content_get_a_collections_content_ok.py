from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.remote_attachment import RemoteAttachment


T = TypeVar("T", bound="GetACollectionsContentGetACollectionsContentOk")


@_attrs_define
class GetACollectionsContentGetACollectionsContentOk:
    """
    Attributes:
        files (list[Attachment | RemoteAttachment]):
        next_ (str): Cursor for next request
    """

    files: list[Attachment | RemoteAttachment]
    next_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.remote_attachment import RemoteAttachment

        files = []
        for files_item_data in self.files:
            files_item: dict[str, Any]
            if isinstance(files_item_data, RemoteAttachment):
                files_item = files_item_data.to_dict()
            else:
                files_item = files_item_data.to_dict()

            files.append(files_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment import Attachment
        from ..models.remote_attachment import RemoteAttachment

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:

            def _parse_files_item(data: object) -> Attachment | RemoteAttachment:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    files_item_type_0 = RemoteAttachment.from_dict(data)

                    return files_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                files_item_type_1 = Attachment.from_dict(data)

                return files_item_type_1

            files_item = _parse_files_item(files_item_data)

            files.append(files_item)

        next_ = d.pop("next")

        get_a_collections_content_get_a_collections_content_ok = cls(
            files=files,
            next_=next_,
        )

        get_a_collections_content_get_a_collections_content_ok.additional_properties = d
        return get_a_collections_content_get_a_collections_content_ok

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
