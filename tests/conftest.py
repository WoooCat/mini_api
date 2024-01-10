import pytest
from peewee import SqliteDatabase
from typer.testing import CliRunner

from src.app import create_app
from src.config import Config, TestingConfig
from src.core.converter import Converter
from src.db.models import db_tables_list, ReportDriver, DetailDriver
from tests.precondition_data import TestData


@pytest.fixture(scope="module")
def runner():
    """Create Typer testing Cli Runner"""
    return CliRunner()


@pytest.fixture(scope="session")
def client():
    """Create Test Flask Client"""
    flask_app = create_app(Config.testing)
    yield flask_app.test_client()


@pytest.fixture(scope="session")
def empty_test_database():
    """Create empty test database with tables"""
    test_db = SqliteDatabase(TestingConfig.SQLITE_DATABASE_URI)
    test_db.bind(db_tables_list)
    test_db.connect()
    test_db.create_tables(db_tables_list)
    yield test_db
    test_db.drop_tables(db_tables_list)
    test_db.close()


@pytest.fixture(scope="session")
def test_database(empty_test_database):
    """Populate test database by test_data"""
    drivers_data = TestData.enum_drivers_ascending
    details_drivers = [Converter.create_detailed_driver_dict(driver) for driver in drivers_data]
    report_drivers = [Converter.create_report_driver_dict(driver) for driver in drivers_data]

    with empty_test_database.atomic():
        ReportDriver.insert_many(report_drivers).execute()
        DetailDriver.insert_many(details_drivers).execute()
    yield empty_test_database
