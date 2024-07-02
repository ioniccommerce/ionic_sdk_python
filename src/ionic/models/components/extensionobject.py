"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .extensionimages import ExtensionImages
from .extensionlinks import ExtensionLinks
from .pricewithcurrency import PriceWithCurrency
from .shippingattribute import ShippingAttribute
from dataclasses_json import Undefined, dataclass_json
from ionic import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExtensionObject:
    images: ExtensionImages = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('images') }})
    links: ExtensionLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('links') }})
    price: PriceWithCurrency = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    shipping_attributes: Optional[List[ShippingAttribute]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_attributes'), 'exclude': lambda f: f is None }})
    

