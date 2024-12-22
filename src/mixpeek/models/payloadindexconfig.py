"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .boolindexparams import BoolIndexParams, BoolIndexParamsTypedDict
from .datetimeindexparams import DatetimeIndexParams, DatetimeIndexParamsTypedDict
from .floatindexparams import FloatIndexParams, FloatIndexParamsTypedDict
from .geoindexparams import GeoIndexParams, GeoIndexParamsTypedDict
from .integerindexparams import IntegerIndexParams, IntegerIndexParamsTypedDict
from .keywordindexparams import KeywordIndexParams, KeywordIndexParamsTypedDict
from .payloadschematype import PayloadSchemaType
from .textindexparams import TextIndexParams, TextIndexParamsTypedDict
from .uuidindexparams import UUIDIndexParams, UUIDIndexParamsTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


FieldSchemaTypedDict = TypeAliasType(
    "FieldSchemaTypedDict",
    Union[
        FloatIndexParamsTypedDict,
        GeoIndexParamsTypedDict,
        DatetimeIndexParamsTypedDict,
        BoolIndexParamsTypedDict,
        KeywordIndexParamsTypedDict,
        UUIDIndexParamsTypedDict,
        IntegerIndexParamsTypedDict,
        TextIndexParamsTypedDict,
    ],
)


FieldSchema = TypeAliasType(
    "FieldSchema",
    Union[
        FloatIndexParams,
        GeoIndexParams,
        DatetimeIndexParams,
        BoolIndexParams,
        KeywordIndexParams,
        UUIDIndexParams,
        IntegerIndexParams,
        TextIndexParams,
    ],
)


class PayloadIndexConfigTypedDict(TypedDict):
    r"""Configuration for a payload index"""

    field_name: str
    type: PayloadSchemaType
    field_schema: NotRequired[Nullable[FieldSchemaTypedDict]]


class PayloadIndexConfig(BaseModel):
    r"""Configuration for a payload index"""

    field_name: str

    type: PayloadSchemaType

    field_schema: OptionalNullable[FieldSchema] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["field_schema"]
        nullable_fields = ["field_schema"]
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
