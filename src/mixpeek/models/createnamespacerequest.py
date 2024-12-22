"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payloadindexconfig import PayloadIndexConfig, PayloadIndexConfigTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class CreateNamespaceRequestTypedDict(TypedDict):
    r"""Request schema for creating a new namespace"""

    namespace_name: str
    r"""Name of the namespace to create"""
    vector_indexes: List[str]
    r"""List of vector indexes to be used within this namespace. Must be one of: 'image', 'multimodal', 'text', 'keyword'"""
    payload_indexes: NotRequired[Nullable[List[PayloadIndexConfigTypedDict]]]
    r"""List of payload index configurations"""


class CreateNamespaceRequest(BaseModel):
    r"""Request schema for creating a new namespace"""

    namespace_name: str
    r"""Name of the namespace to create"""

    vector_indexes: List[str]
    r"""List of vector indexes to be used within this namespace. Must be one of: 'image', 'multimodal', 'text', 'keyword'"""

    payload_indexes: OptionalNullable[List[PayloadIndexConfig]] = UNSET
    r"""List of payload index configurations"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["payload_indexes"]
        nullable_fields = ["payload_indexes"]
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
