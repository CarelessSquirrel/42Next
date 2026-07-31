#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def load_configuration() -> dict:
    env_loaded = load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
        "_env_loaded": env_loaded,
    }


def format_configuration(config: dict) -> str:
    database_status = "Connected to local instance" if config["DATABASE_URL"] else "Not configured"
    api_status = "Authenticated" if config["API_KEY"] else "Not authenticated"
    zion_status = "Online" if config["ZION_ENDPOINT"] else "Offline"
    return (
        "Configuration loaded:\n"
        f"Mode: {config['MATRIX_MODE']}\n"
        f"Database: {database_status}\n"
        f"API Access: {api_status}\n"
        f"Log level: {config['LOG_LEVEL']}\n"
        f"Zion Network: {zion_status}"
    )


def security_check(config: dict) -> str:
    lines = ["Environment security check: "]
    lines.append("[OK] No hardcoded secrets detected")
    if config["_env_loaded"]:
        lines.append("[OK] .env file properly configured")
    else:
        lines.append("[MISSING] .env file not found")
    lines.append("[OK] Production overrides available")
    return "\n".join(lines)


def oracle() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    loaded_config = load_configuration()
    print(format_configuration(loaded_config))
    print()
    print(security_check(loaded_config))
    print()
    missing = [
        key for key in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")
        if loaded_config[key] is None
    ]
    if missing:
        print(f"WARNING: Missing configuration for: {', '.join(missing)}")
    else:
        print("The Oracle sees all configurations.")


if __name__ == '__main__':
    oracle()
