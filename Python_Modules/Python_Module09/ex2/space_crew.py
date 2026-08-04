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
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int =Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission