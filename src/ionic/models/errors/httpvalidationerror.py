"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import validationerror as components_validationerror
from dataclasses_json import Undefined, dataclass_json
from ionic import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class HTTPValidationError(Exception):
    detail: Optional[List[components_validationerror.ValidationError]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail'), 'exclude': lambda f: f is None }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self)