# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.function_object import FunctionObject


class AssistantToolsFunction(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AssistantToolsFunction - a model defined in OpenAPI

        type: The type of this AssistantToolsFunction.
        function: The function of this AssistantToolsFunction.
    """

    type: str = Field(alias="type")
    function: FunctionObject = Field(alias="function")

AssistantToolsFunction.update_forward_refs()