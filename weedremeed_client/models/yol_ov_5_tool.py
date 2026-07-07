from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.yol_ov_5_tool_model import YOLOv5ToolModel

T = TypeVar("T", bound="YOLOv5Tool")


@_attrs_define
class YOLOv5Tool:
    """Runs object detection on the image collection using a custom YOLOv5 model

    Attributes:
        model (YOLOv5ToolModel):
        threshold (float): Minimum Confidence Threshold
        save_images (bool):
    """

    model: YOLOv5ToolModel
    threshold: float
    save_images: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model.value

        threshold = self.threshold

        save_images = self.save_images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "threshold": threshold,
                "save_images": save_images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = YOLOv5ToolModel(d.pop("model"))

        threshold = d.pop("threshold")

        save_images = d.pop("save_images")

        yol_ov_5_tool = cls(
            model=model,
            threshold=threshold,
            save_images=save_images,
        )

        yol_ov_5_tool.additional_properties = d
        return yol_ov_5_tool

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
