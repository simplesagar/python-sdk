"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class InputType(str, Enum):
    URL = "url"
    TEXT = "text"
    FILE = "file"
    BASE64 = "base64"