#!/usr/bin/env python3

import json
from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_safety(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        command_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        if not any(member.rank in command_ranks for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew validation")
    print("=" * 40)
    data_dir = Path(__file__).parent.parent / "generated_data"

    with open(data_dir / "space_missions.json") as f:
        records = json.load(f)
    for record in records:
        try:
            mission = SpaceMission(**record)
            break
        except ValidationError:
            continue
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: {mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )

    print("\n" + "=" * 40)
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_LUNA",
            mission_name="Lunar Survey Mission",
            destination="Moon",
            launch_date=datetime.fromisoformat("2024-11-01T09:00:00"),
            duration_days=180,
            budget_millions=150.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah",
                    rank=Rank.LIEUTENANT,
                    age=30,
                    specialization="Navigation",
                    years_experience=5,
                ),
            ],
        )
    except ValidationError as e:
        for failure in e.errors():
            print(failure["msg"])


if __name__ == "__main__":
    main()
