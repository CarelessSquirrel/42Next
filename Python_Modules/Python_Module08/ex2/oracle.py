#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def load_configuration() -> dict:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def format_configuration(config: dict) -> str:
    database_status = "Connected to local instance" if config["DATABASE_URL"] else "Not configured"
    api_status = "Authenticated" if config["API_KEY"] else "Not authenticated"
    zion_status = "Online" if config["ZION_ENDPOINT"] else "Offline"
    return (
        "Configuration"
    )


def security_check(config: dict) -> str:
    ...


def oracle() -> None:
    print(load_configuration())

if __name__ == '__main__':
    oracle()
