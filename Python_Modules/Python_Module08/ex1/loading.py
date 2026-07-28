#!/usr/bin/env python3

from __future__ import annotations
import importlib
from typing import TYPE_CHECKING
import os

if TYPE_CHECKING:
    import pandas as pd


def import_handler() -> dict:
    accumulator = {}
    packages = [
        "pandas",
        "numpy",
        "matplotlib",
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
        return None
    url = (
        "https://api.worldbank.org/v2/country/all/indicator/"
        "SP.POP.TOTL?format=json&per_page=300&date=2022"
    )
    try:
        r = requests_module.get(url)
        r.raise_for_status()
        data = r.json()
    except requests_module.exceptions.RequestException as e:
        print(f"Your API request has failed: {e}")
        return None
    return data[1]


def fallback_data_gen(modules: dict) -> list | None:
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
    populations = numpy_module.random.randint(
        100_000, 1_500_000_000, size=len(country_names)
    )
    fallback = []
    for name, pop in zip(country_names, populations):
        fallback.append({"country": {"value": name}, "value": int(pop)})
    return fallback


def get_dataset(modules: dict) -> list | None:
    data = api_call(modules)
    if data is not None:
        return data
    print("Falling back to simulated data..")
    return fallback_data_gen(modules)


def data_modification(modules: dict, data: list[dict]) -> pd.DataFrame | None:
    panda_module = modules.get("pandas")
    if panda_module is None:
        print("pandas unavailable, unavailable to modify data")
        return None
    try:
        df = panda_module.json_normalize(data)
        df = df.sort_values(by="value", ascending=False)
        df = df.head(10)
        df = df.rename(
            columns={"country.value": "country", "value": "population"}
        )
    except KeyError as e:
        print(f"Expected column missing from data: {e}")
        return None
    return df


DESCRIPTIONS = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def print_dependency_report(modules: dict) -> None:
    print("Checking dependencies:")
    for name, description in DESCRIPTIONS.items():
        mod = modules.get(name)
        if mod is None:
            print(f"[MISSING] {name} - not installed")
        else:
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")


def visualize_data(modules: dict, df: pd.DataFrame) -> bool:
    plt_module = modules.get("matplotlib.pyplot")
    if plt_module is None:
        print("matplotlib unavailable, unable to generate visualization")
        return False
    plt_module.figure(figsize=(10, 6))
    plt_module.bar(df["country"], df["population"])
    plt_module.xlabel("Country")
    plt_module.ylabel("Population")
    plt_module.title("Matrix Data Analysis: Top 10 Most Populous Countries")
    plt_module.xticks(rotation=45, ha="right")
    plt_module.tight_layout()
    output_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "matrix_analysis.png"
    )
    plt_module.savefig(output_path)
    return True


def print_dependency_management_comparison() -> None:
    print("Dependency management comparison:")
    print("  pip + requirements.txt:")
    print("    - flat list, exact pins (e.g. pandas==2.3.3)")
    print("    - install with: pip install -r requirements.txt")
    print("    - no built-in lock file; you manage the venv yourself")
    print("  Poetry + pyproject.toml:")
    print("    - structured, flexible constraints (e.g. pandas = \"^2.3.3\")")
    print("    - install with: poetry install")
    print("    - auto-generates poetry.lock (exact resolved versions)")
    print("    - manages its own venv automatically")


def matrix() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    modules = import_handler()
    print_dependency_report(modules)
    print()
    print_dependency_management_comparison()
    print()

    print("Analyzing Matrix data...")
    data = get_dataset(modules)
    if data is None:
        print("No data available - all sources failed")
        return
    print(f"Processing {len(data)} data points...")

    df = data_modification(modules, data)
    if df is None:
        print("Unable to process data")
        return

    print("Generating visualization...")
    if visualize_data(modules, df):
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")


if __name__ == '__main__':
    matrix()
