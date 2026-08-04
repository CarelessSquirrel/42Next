#!/usr/bin/env python3

from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError, 
from enum import Enum
from typing import Optional


class Rank(str, Enum):
    CADET="cadet"
    OFFICER="officer"
    LIEUTENANT="lieutenant"
    CAPTAIN="captain"
    COMMANDER="commander"


class CrewMember(BaseModel):
    member_id