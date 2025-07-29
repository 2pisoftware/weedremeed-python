from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PresetPickerTool")


@_attrs_define
class PresetPickerTool:
    """Runs preset colour range detection on an uploaded image collection

    Attributes:
        range_ (list[list[int]]): Min/Max pair of vectors for detection range in colour space. Length 2 array containing
            3 length arrays with integers.
    """

    range_: list[list[int]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        range_ = []
        for range_item_data in self.range_:
            range_item = range_item_data

            range_.append(range_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "range": range_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        range_ = []
        _range_ = d.pop("range")
        for range_item_data in _range_:
            range_item = cast(list[int], range_item_data)

            range_.append(range_item)

        preset_picker_tool = cls(
            range_=range_,
        )

        preset_picker_tool.additional_properties = d
        return preset_picker_tool

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
