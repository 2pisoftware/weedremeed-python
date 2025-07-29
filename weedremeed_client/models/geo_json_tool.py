from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GeoJsonTool")


@_attrs_define
class GeoJsonTool:
    """Collates detection results into GeoJSON format

    Attributes:
        top_bearing (int): Flight yaw/orientation, degrees from North
        cm_per_pixel (float): Image to ground distance as centimetres per pixel
    """

    top_bearing: int
    cm_per_pixel: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_bearing = self.top_bearing

        cm_per_pixel = self.cm_per_pixel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "top_bearing": top_bearing,
                "cm_per_pixel": cm_per_pixel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        top_bearing = d.pop("top_bearing")

        cm_per_pixel = d.pop("cm_per_pixel")

        geo_json_tool = cls(
            top_bearing=top_bearing,
            cm_per_pixel=cm_per_pixel,
        )

        geo_json_tool.additional_properties = d
        return geo_json_tool

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
