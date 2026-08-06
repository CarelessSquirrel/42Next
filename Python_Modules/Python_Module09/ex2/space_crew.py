#!/usr/bin/env python3

from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
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
            raise ValueError("Mission must have atleast one Commander or Captain")
        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (>365 days) need 50% experienced crew(5+ years)"
                )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self



def main() -> None:
    print("Space Mission Crew validation")
    print("=" * 40)
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2024-11-01T09:00:00"),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah",
                rank=Rank.COMMANDER,
                age=42,
                specialization="Mission lead",
                years_experience=15,
            ),
            CrewMember(
                member_id="CM002",
                name="John",
                rank=Rank.CADET,
                age=24,
                specialization="Engineer",
                years_experience=5,
            ),
            CrewMember(
                member_id="CM003",
                name="Lydia",
                rank=Rank.CAPTAIN,
                age=50,
                specialization="Captain",
                years_experience=20,
            ),
        ],
    )
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: {valid_mission.budget_millions}M")
    print(f"Crew size: {valid_mission.crew}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(f"- {member.name} ({member.rank.value}) - {member.specialization})")
    print("\n" + ('=' * 40))
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-11-01T09:00:00"),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah",
                    rank=Rank.CADET,
                    age=17,
                    specialization="Mission lead",
                    years_experience=0,
                ),
            ],
        )
    except ValidationError as e:
        for failure in e.errors():
            print(failure["msg"])

if __name__ == '__main__':
    main()