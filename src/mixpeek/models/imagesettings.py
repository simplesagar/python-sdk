"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .embeddingrequest import EmbeddingRequest, EmbeddingRequestTypedDict
from .imagedescribesettings import ImageDescribeSettings, ImageDescribeSettingsTypedDict
from .imagedetectsettings import ImageDetectSettings, ImageDetectSettingsTypedDict
from .imagereadsettings import ImageReadSettings, ImageReadSettingsTypedDict
from .jsonimageoutputsettings import (
    JSONImageOutputSettings,
    JSONImageOutputSettingsTypedDict,
)
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ImageSettingsTypedDict(TypedDict):
    read: NotRequired[Nullable[ImageReadSettingsTypedDict]]
    r"""Settings for reading and analyzing image content."""
    embed: NotRequired[List[EmbeddingRequestTypedDict]]
    r"""List of embedding settings for generating multiple embeddings. If url is provided, value must be None.
    Default: [{type: 'url', vector_index: 'multimodal'}] if none provided.
    """
    describe: NotRequired[Nullable[ImageDescribeSettingsTypedDict]]
    r"""Settings for generating image descriptions."""
    detect: NotRequired[Nullable[ImageDetectSettingsTypedDict]]
    r"""Settings for object detection in images."""
    json_output: NotRequired[Nullable[JSONImageOutputSettingsTypedDict]]
    r"""Settings for structured JSON output of image analysis."""


class ImageSettings(BaseModel):
    read: OptionalNullable[ImageReadSettings] = UNSET
    r"""Settings for reading and analyzing image content."""

    embed: Optional[List[EmbeddingRequest]] = None
    r"""List of embedding settings for generating multiple embeddings. If url is provided, value must be None.
    Default: [{type: 'url', vector_index: 'multimodal'}] if none provided.
    """

    describe: OptionalNullable[ImageDescribeSettings] = UNSET
    r"""Settings for generating image descriptions."""

    detect: OptionalNullable[ImageDetectSettings] = UNSET
    r"""Settings for object detection in images."""

    json_output: OptionalNullable[JSONImageOutputSettings] = UNSET
    r"""Settings for structured JSON output of image analysis."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["read", "embed", "describe", "detect", "json_output"]
        nullable_fields = ["read", "describe", "detect", "json_output"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m