"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class PayloadSchemaType(str, Enum):
    KEYWORD = "keyword"
    INTEGER = "integer"
    FLOAT = "float"
    BOOL = "bool"
    GEO = "geo"
    DATETIME = "datetime"
    TEXT = "text"
    UUID = "uuid"
