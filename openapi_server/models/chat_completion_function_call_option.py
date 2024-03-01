# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ChatCompletionFunctionCallOption(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ChatCompletionFunctionCallOption - a model defined in OpenAPI

        name: The name of this ChatCompletionFunctionCallOption.
    """

    name: str = Field(alias="name")

ChatCompletionFunctionCallOption.update_forward_refs()