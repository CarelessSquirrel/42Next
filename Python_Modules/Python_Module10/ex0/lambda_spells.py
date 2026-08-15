#!/usr/bin/env python3
artifacts_list = [
    {'name': 'crystal', 'power': 86, 'type': 'gem'},
    {'name': 'prismarine', 'power': 77, 'type': 'gem'}
]

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    descending = sorted(artifacts, key=lambda a: a['power'], reverse=True)
    return descending


sorted_list = artifact_sorter(artifacts_list)
for artifact in sorted_list:
    print(artifact['power'])