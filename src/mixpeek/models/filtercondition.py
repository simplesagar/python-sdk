"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, Optional
from typing_extensions import NotRequired, TypedDict


class Operator(str, Enum):
    r"""Comparison operator"""

    EQ = "eq"
    NE = "ne"
    GT = "gt"
    LT = "lt"
    GTE = "gte"
    LTE = "lte"
    IN = "in"
    NIN = "nin"
    IS_NULL = "is_null"
    TEXT = "text"
    EXISTS = "exists"


class FilterConditionTypedDict(TypedDict):
    key: str
    r"""Field name to filter on"""
    value: NotRequired[Nullable[Any]]
    r"""Value to compare against"""
    operator: NotRequired[Operator]
    r"""Comparison operator"""


class FilterCondition(BaseModel):
    key: str
    r"""Field name to filter on"""

    value: OptionalNullable[Any] = UNSET
    r"""Value to compare against"""

    operator: Optional[Operator] = Operator.EQ
    r"""Comparison operator"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["value", "operator"]
        nullable_fields = ["value"]
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
