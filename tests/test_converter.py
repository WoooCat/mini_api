from unittest.mock import patch

from src.core.converter import Converter
from tests.precondition_data import TestData


def test_create_detailed_driver_dict():
    test_data = TestData.driver_with_position
    expected = TestData.detail_driver_json
    actual = Converter.create_detailed_driver_dict(test_data)
    assert actual == expected


def test_create_report_driver_dict():
    expected = TestData.report_driver_json
    actual = Converter.create_report_driver_dict(TestData.driver_with_position)
    assert actual == expected


def test_driver_to_xml():
    assert Converter.driver_to_xml(TestData.detail_driver_json) == TestData.detail_driver_xml


def test_formatting_data_json():
    test_data = TestData.detail_driver_json
    assert Converter.formatting_data("json", test_data) == TestData.detail_driver_json


@patch("src.core.converter.Converter.driver_to_xml", return_value=TestData.detail_driver_xml)
def test_formatting_data_xml(mock_driver_to_xml):
    test_data = TestData.detail_driver_json
    assert Converter.formatting_data("xml", test_data) == TestData.detail_driver_xml
    mock_driver_to_xml.assert_called_once()


@patch("src.core.converter.Converter.formatting_data", return_value=TestData.list_of_drivers_dict_report)
def test_convert_data_to_format_json_report(mock_formatting_data):
    assert (
        Converter.convert_data_to_format(TestData.enum_drivers_ascending, format_type="json")
        == TestData.list_of_drivers_dict_report
    )
    mock_formatting_data.assert_called_once()


@patch("src.core.converter.Converter.formatting_data", return_value=TestData.list_of_drivers_xml_report)
def test_get_multi_drivers_in_format_xml_report(mock_formatting_data):
    assert (
        Converter.convert_data_to_format(TestData.enum_drivers_ascending, format_type="xml")
        == TestData.list_of_drivers_xml_report
    )
    mock_formatting_data.assert_called_once()
