#!/usr/bin/env python3
artifacts_list = [
    {'name': 'Fire Staff', 'power': 92, 'type': 'Physical'},
    {'name': 'Crystal Orb', 'power': 85, 'type': 'Magic'}
]

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    descending = sorted(artifacts, key=lambda a: a['power'], reverse=True)
    return descending


def main() -> None:
    sa = artifact_sorter(artifacts_list)
    print("Testing artifact sorter...")
    print(f"{sa[0]['name']} ({sa[0]['power']} power) comes before {sa[1]['name']} ({sa[1]['power']} power)")

main()