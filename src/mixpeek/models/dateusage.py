"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .actionusage import ActionUsage, ActionUsageTypedDict
from mixpeek.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class DateUsageTypedDict(TypedDict):
    date_: str
    credits: int
    actions: List[ActionUsageTypedDict]


class DateUsage(BaseModel):
    date_: Annotated[str, pydantic.Field(alias="date")]

    credits: int

    actions: List[ActionUsage]
