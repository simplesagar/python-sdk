"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .validationerror import ValidationError
from mixpeek import utils
from mixpeek.types import BaseModel
from typing import List, Optional


class HTTPValidationErrorData(BaseModel):
    detail: Optional[List[ValidationError]] = None


class HTTPValidationError(Exception):
    data: HTTPValidationErrorData

    def __init__(self, data: HTTPValidationErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, HTTPValidationErrorData)
