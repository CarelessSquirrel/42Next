#!/usr/bin/env python3

import sys
import importlib


def import_handler() -> dict:
    accumulator = {}
    packages = [
        "pandas",
        "numpy",
        "matplotlib.pyplot",
        "requests"
    ]
    for module in packages:
        try:
            mod = importlib.import_module(module)
            accumulator[module] = mod
        except ImportError as e:
            print(f"{module} could not be loaded: {e}")
    return accumulator


def api_call(modules: dict) -> list | None:
    requests_module = modules.get("requests")
    if requests_module is None:
        print("requests unavailable, unable to fetch data")
        return
    try:
        r = requests_module.get("https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=300&date=2022")
        r.raise_for_status()
        data = r.json()
    except requests_module.exceptions.RequestException as e:
        print(f"Your API request has failed: {e}")
        return
    return data[1]


def fallback_data_gen(modules: dict) -> list:
    numpy_module = modules.get("numpy")
    if numpy_module is None:
        print("numpy unavailable, unable to generate fallback data")
        return None
    country_names = [
        "The Netherlands",
        "Germany",
        "Belgium",
        "UK",
        "France",
        "Switzerland",
        "Poland"
    ]
    populations = numpy_module.random.randint(100_000, 1_500_000_000, size=len(country_names))
    fallback = []
    for name, pop in zip(country_names, populations):
        fallback.append({"country": {"value": name}, "value": int(pop)})
    return fallback


def get_dataset(modules: dict) -> list | None:
    data = api_call(modules)
    if data is not None:
        return data
    print("Falling back to simulated data..")
    fallback_data_gen(modules)


def data_modification(modules: dict, data: list[dict]) -> list | None:
    panda_module = modules.get("pandas")
    if panda_module is None:
        print("pandas unavailable, unavailable to modify data")
        return
    try:
        df = panda_module.json_normalize(data)
        df.sort_values(by="country.value", ascending=False)
        df.describe()

def matrix():
    ...


if __name__ == '__main__':
    matrix()