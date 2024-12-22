"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .groupbyoptions import GroupByOptions, GroupByOptionsTypedDict
from .logicaloperator_output import (
    LogicalOperatorOutput,
    LogicalOperatorOutputTypedDict,
)
from .rerankingoptions import RerankingOptions, RerankingOptionsTypedDict
from .searchquery_output import SearchQueryOutput, SearchQueryOutputTypedDict
from .sortoption import SortOption, SortOptionTypedDict
from mixpeek.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class SearchRequestFeaturesOutputTypedDict(TypedDict):
    queries: List[SearchQueryOutputTypedDict]
    r"""List of search queries to perform.

    Behavior:
    - Single query: Results are returned directly from that query
    - Multiple queries: Results are combined using Reciprocal Rank Fusion (RRF)

    RRF combines results from multiple queries by:
    1. Taking each item's rank position in each result list
    2. Re-ranking all items by their combined RRF scores

    When merging lists from different sources,
    RRF considers all items that appear in any of the input lists,
    not just items that appear in all lists.

    This helps surface items that rank well across multiple queries while
    reducing the impact of outlier high rankings in single queries.

    NOTE: If query array is empty, it will return all features.


    """
    collections: List[str]
    r"""List of Collection names to search within, required"""
    filters: NotRequired[Nullable[LogicalOperatorOutputTypedDict]]
    r"""Used for filtering across all indexes"""
    group_by: NotRequired[Nullable[GroupByOptionsTypedDict]]
    r"""Grouping options for search results"""
    sort: NotRequired[Nullable[SortOptionTypedDict]]
    r"""List of fields to sort by, with direction (asc or desc). Supports dot notation for nested fields."""
    select: NotRequired[Nullable[List[str]]]
    r"""List of fields to return in results, supports dot notation. If None, all fields are returned."""
    reranking_options: NotRequired[Nullable[RerankingOptionsTypedDict]]
    r"""Options for ranking the search results, including weights and feedback application"""
    session_id: NotRequired[Nullable[str]]
    r"""Identifier for tracking search session interactions"""
    return_url: NotRequired[Nullable[bool]]
    r"""Return the presigned URL for the asset and preview asset, this will introduce additional latency"""


class SearchRequestFeaturesOutput(BaseModel):
    queries: List[SearchQueryOutput]
    r"""List of search queries to perform.

    Behavior:
    - Single query: Results are returned directly from that query
    - Multiple queries: Results are combined using Reciprocal Rank Fusion (RRF)

    RRF combines results from multiple queries by:
    1. Taking each item's rank position in each result list
    2. Re-ranking all items by their combined RRF scores

    When merging lists from different sources,
    RRF considers all items that appear in any of the input lists,
    not just items that appear in all lists.

    This helps surface items that rank well across multiple queries while
    reducing the impact of outlier high rankings in single queries.

    NOTE: If query array is empty, it will return all features.


    """

    collections: List[str]
    r"""List of Collection names to search within, required"""

    filters: OptionalNullable[LogicalOperatorOutput] = UNSET
    r"""Used for filtering across all indexes"""

    group_by: OptionalNullable[GroupByOptions] = UNSET
    r"""Grouping options for search results"""

    sort: OptionalNullable[SortOption] = UNSET
    r"""List of fields to sort by, with direction (asc or desc). Supports dot notation for nested fields."""

    select: OptionalNullable[List[str]] = UNSET
    r"""List of fields to return in results, supports dot notation. If None, all fields are returned."""

    reranking_options: OptionalNullable[RerankingOptions] = UNSET
    r"""Options for ranking the search results, including weights and feedback application"""

    session_id: OptionalNullable[str] = UNSET
    r"""Identifier for tracking search session interactions"""

    return_url: OptionalNullable[bool] = UNSET
    r"""Return the presigned URL for the asset and preview asset, this will introduce additional latency"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "filters",
            "group_by",
            "sort",
            "select",
            "reranking_options",
            "session_id",
            "return_url",
        ]
        nullable_fields = [
            "filters",
            "group_by",
            "sort",
            "select",
            "reranking_options",
            "session_id",
            "return_url",
        ]
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
