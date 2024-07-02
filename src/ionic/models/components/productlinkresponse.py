"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .enrichedproduct import EnrichedProduct
from dataclasses_json import Undefined, dataclass_json
from ionic import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProductLinkResponse:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    product: EnrichedProduct = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product') }})
    idempotency_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('idempotency_key'), 'exclude': lambda f: f is None }})
    reference_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference_id'), 'exclude': lambda f: f is None }})
    

