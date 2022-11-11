from pathlib import Path
import configparser
import os

ENVIRONMENT = os.environ.setdefault("SPLIT_WISER", "development")

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR.parent / "resources"

CONFIG = configparser.ConfigParser()
CONFIG.read(RESOURCES_DIR / f"{ENVIRONMENT}.ini")

DEBUG = CONFIG.getboolean("DEFAULT", "DEBUG")
