"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import error as components_error
from ...models.components import pet as components_pet
from typing import Dict, List, Optional


@dataclasses.dataclass
class ListPetsRequest:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many items to return at one time (max 100)"""
    



@dataclasses.dataclass
class ListPetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[components_error.Error] = dataclasses.field(default=None)
    r"""unexpected error"""
    pets: Optional[List[components_pet.Pet]] = dataclasses.field(default=None)
    r"""A paged array of pets"""
    

