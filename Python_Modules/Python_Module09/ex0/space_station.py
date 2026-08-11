#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pathlib import Path
import json
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    data_dir = Path(__file__).parent.parent / "generated_data"

    with open(data_dir / "space_stations.json") as f:
        records = json.load(f)
    for record in records:
        try:
            station = SpaceStation(**record)
            break
        except ValidationError:
            continue
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Offline"
    print(f"Status: {status}")

    print("\n" + "=" * 40)
    with open(data_dir / "invalid_stations.json") as f:
        invalid_records = json.load(f)
    print("Expected validation error:")
    for bad_record in invalid_records:
        try:
            SpaceStation(**bad_record)
        except ValidationError as e:
            for err in e.errors():
                print(f"{err['loc'][0]}: {err['msg']}")


if __name__ == "__main__":
    main()
