"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payloadindexconfig import PayloadIndexConfig, PayloadIndexConfigTypedDict
from mixpeek.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class UpdateNamespaceRequestTypedDict(TypedDict):
    r"""Request schema for updating a namespace's payload indexes"""

    namespace_name: str
    r"""Name of the namespace to update"""
    payload_indexes: List[PayloadIndexConfigTypedDict]
    r"""Updated list of payload index configurations"""


class UpdateNamespaceRequest(BaseModel):
    r"""Request schema for updating a namespace's payload indexes"""

    namespace_name: str
    r"""Name of the namespace to update"""

    payload_indexes: List[PayloadIndexConfig]
    r"""Updated list of payload index configurations"""
