from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.colour_picker_tool_colour_space import ColourPickerToolColourSpace
from ..types import UNSET, Unset

T = TypeVar("T", bound="ColourPickerTool")


@_attrs_define
class ColourPickerTool:
    """Run colour detection

    Attributes:
        attachment_id (str):
        discrim_bands (float):
        retention (int):
        colour_space (ColourPickerToolColourSpace):
        bound_dilation (int): detection expansion (pixels)
        bound_colour (str | Unset):
        pen_weight (float | Unset):
        max_collation (str | Unset):
    """

    attachment_id: str
    discrim_bands: float
    retention: int
    colour_space: ColourPickerToolColourSpace
    bound_dilation: int
    bound_colour: str | Unset = UNSET
    pen_weight: float | Unset = UNSET
    max_collation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachment_id = self.attachment_id

        discrim_bands = self.discrim_bands

        retention = self.retention

        colour_space = self.colour_space.value

        bound_dilation = self.bound_dilation

        bound_colour = self.bound_colour

        pen_weight = self.pen_weight

        max_collation = self.max_collation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attachment_id": attachment_id,
                "discrim_bands": discrim_bands,
                "retention": retention,
                "colour_space": colour_space,
                "bound_dilation": bound_dilation,
            }
        )
        if bound_colour is not UNSET:
            field_dict["bound_colour"] = bound_colour
        if pen_weight is not UNSET:
            field_dict["pen_weight"] = pen_weight
        if max_collation is not UNSET:
            field_dict["max_collation"] = max_collation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_id = d.pop("attachment_id")

        discrim_bands = d.pop("discrim_bands")

        retention = d.pop("retention")

        colour_space = ColourPickerToolColourSpace(d.pop("colour_space"))

        bound_dilation = d.pop("bound_dilation")

        bound_colour = d.pop("bound_colour", UNSET)

        pen_weight = d.pop("pen_weight", UNSET)

        max_collation = d.pop("max_collation", UNSET)

        colour_picker_tool = cls(
            attachment_id=attachment_id,
            discrim_bands=discrim_bands,
            retention=retention,
            colour_space=colour_space,
            bound_dilation=bound_dilation,
            bound_colour=bound_colour,
            pen_weight=pen_weight,
            max_collation=max_collation,
        )

        colour_picker_tool.additional_properties = d
        return colour_picker_tool

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
