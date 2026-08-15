#!/usr/bin/env python3
artifacts_list = [
    {'name': 'Fire Staff', 'power': 92, 'type': 'Physical'},
    {'name': 'Crystal Orb', 'power': 85, 'type': 'Magic'}
]

mage_dict = [
    {'name': 'John', 'power': 77, 'element': 'Water'},
    {'name': 'Claire', 'power': 83, "element": 'Fire'}
]

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    descending = sorted(artifacts, key=lambda a: a['power'], reverse=True)
    return descending


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = filter(lambda x: if x >= min_power, x['power'])


def main() -> None:
    sa = artifact_sorter(artifacts_list)
    print("Testing artifact sorter...")
    print(f"{sa[0]['name']} ({sa[0]['power']} power) comes before {sa[1]['name']} ({sa[1]['power']} power)")

main()