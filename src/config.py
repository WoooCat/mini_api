from enum import Enum

from settings import Settings


class Configuration:
    """APP Configuration"""

    DEBUG = False
    TESTING = False
    SQLITE_DATABASE_URI = ""


class DevelopmentConfig(Configuration):
    DEBUG = True
    SQLITE_DATABASE_URI = Settings.DB


class TestingConfig(Configuration):
    DEBUG = True
    TESTING = True
    SQLITE_DATABASE_URI = ":memory:"


class Config(str, Enum):
    development = "development"
    testing = "testing"


config = {
    Config.development: DevelopmentConfig,
    Config.testing: TestingConfig,
}
