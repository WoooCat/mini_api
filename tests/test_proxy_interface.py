from unittest.mock import patch

from src.core.proxy_interface import MyReportRacing
from tests.precondition_data import TestData


@patch("src.core.proxy_interface.build_report", return_value=TestData.drivers_sorted)
def test_get_drivers_ascending(mocked_build_report):
    path = "/path/to/dir"
    report = MyReportRacing(path)
    actual = report.get_drivers()
    expected = TestData.enum_drivers_ascending
    assert actual == expected
    mocked_build_report.assert_called_once()


@patch("src.core.proxy_interface.build_report", return_value=TestData.drivers_sorted)
def test_get_drivers_descending(mocked_build_report):
    path = "/path/to/dir"
    report = MyReportRacing(path)
    actual = report.get_drivers(order="desc")
    expected = TestData.enum_drivers_descending
    assert actual == expected
    mocked_build_report.assert_called_once()


@patch("src.core.proxy_interface.build_report")
def test_add_drivers_position_asc(mocked_build_report):
    path = "/path/to/dir"
    report = MyReportRacing(path)
    test_data = TestData.drivers_sorted
    expected = TestData.enum_drivers_ascending
    actual = report.add_drivers_position(test_data)
    assert actual == expected
    mocked_build_report.assert_called_once()


@patch("src.core.proxy_interface.build_report")
def test_add_drivers_position_desc(mocked_build_report):
    path = "/path/to/dir"
    report = MyReportRacing(path)
    test_data = TestData.drivers_sorted
    expected = TestData.enum_drivers_descending
    assert report.add_drivers_position(test_data, reverse=True) == expected
    mocked_build_report.assert_called_once()
