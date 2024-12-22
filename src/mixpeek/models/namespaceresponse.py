"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mixpeek.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import TypedDict


class PayloadIndexesTypedDict(TypedDict):
    pass


class PayloadIndexes(BaseModel):
    pass


class NamespaceResponseTypedDict(TypedDict):
    namespace_id: str
    namespace_name: str
    vector_indexes: List[str]
    payload_indexes: Nullable[PayloadIndexesTypedDict]


class NamespaceResponse(BaseModel):
    namespace_id: str

    namespace_name: str

    vector_indexes: List[str]

    payload_indexes: Nullable[PayloadIndexes]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
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
