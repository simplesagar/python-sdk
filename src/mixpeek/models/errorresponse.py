"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .errordetail import ErrorDetail
from mixpeek import utils
from mixpeek.types import BaseModel
from typing import Optional


class ErrorResponseData(BaseModel):
    status: int

    error: ErrorDetail

    success: Optional[bool] = False


class ErrorResponse(Exception):
    data: ErrorResponseData

    def __init__(self, data: ErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorResponseData)
