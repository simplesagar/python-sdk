"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tokenizertype import TokenizerType
from mixpeek.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class TextIndexParamsTypedDict(TypedDict):
    r"""Configuration for text index"""

    type: NotRequired[str]
    tokenizer: NotRequired[TokenizerType]
    min_token_len: NotRequired[int]
    max_token_len: NotRequired[int]
    lowercase: NotRequired[bool]


class TextIndexParams(BaseModel):
    r"""Configuration for text index"""

    type: Optional[str] = "text"

    tokenizer: Optional[TokenizerType] = None

    min_token_len: Optional[int] = 2

    max_token_len: Optional[int] = 15

    lowercase: Optional[bool] = True
