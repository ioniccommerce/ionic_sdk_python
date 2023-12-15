"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from ionic import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Session:
    locale: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('locale') }})
    session_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('session_id') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    

