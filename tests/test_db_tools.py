from unittest.mock import patch
from src.db.db_tools import to_insert_data, to_create_tables
from src.db.models import db_tables_list
from tests.precondition_data import TestData


@patch("src.db.db_tools.db.create_tables")
@patch("src.db.db_tools.db.init")
def test_to_create_tables(mock_init, mock_create_tables):
    assert to_create_tables() is None
    mock_create_tables.assert_called_once()
    mock_init.assert_called_once()


@patch("src.db.db_tools.db.atomic")
@patch("src.db.db_tools.MyReportRacing.get_drivers", return_value=TestData.enum_drivers_ascending)
@patch("src.db.db_tools.MyReportRacing")
def test_to_insert_data(mock_my_report_racing, mock_get_drivers, mock_atomic, empty_test_database):
    assert to_insert_data(db_tables_list) is None
    mock_my_report_racing.assert_called_once()
    mock_get_drivers.assert_not_called()
    mock_atomic.assert_called_once()
