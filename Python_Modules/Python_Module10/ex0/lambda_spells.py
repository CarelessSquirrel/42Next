#!/usr/bin/env python3
artifacts_list = [
    {'name': 'crystal', 'power': 86, 'type': 'gem'},
    {'name': 'prismarine', 'power': 77, 'type': 'gem'}
]

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    descending = sorted(artifacts, key=lambda a: a['power'], reverse=True)

print(artifact_sorter(artifacts_list))