from pathlib import Path
import configparser
import os

ENV = os.environ.setdefault("SPLIT_WISER", "development")

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR.parent / "resources"

CONFIG = configparser.ConfigParser()
CONFIG.read(RESOURCES_DIR / f"{ENV}.ini")

DEBUG = CONFIG.getboolean("DEFAULT", "DEBUG")
SQLALCHEMY_DATABASE_URI = CONFIG.get("DEFAULT", "SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = CONFIG.getboolean(
    "DEFAULT", "SQLALCHEMY_TRACK_MODIFICATIONS"
)
