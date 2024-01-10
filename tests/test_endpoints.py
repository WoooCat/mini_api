from unittest.mock import patch

from tests.precondition_data import TestData
from tests.utils import combined_assertions_json, combined_assertions_xml


@patch("src.core.db_tools.DbFormatter.select_fields_from_db_model", return_value=TestData.report_drivers_asc_json)
def test_get_report_without_args(mock_select_fields_from_db_model, client):
    response = client.get("/api/v1/report")
    expected = TestData.report_drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)
    mock_select_fields_from_db_model.assert_called_once()


@patch("src.core.db_tools.DbFormatter.select_fields_from_db_model", return_value=TestData.report_drivers_asc_json)
def test_get_report_format_json_order_asc(mock_select_dicts_from_db_model, client):
    response = client.get("/api/v1/report?order=asc&format=json")
    expected = TestData.report_drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)
    mock_select_dicts_from_db_model.assert_called_once()


@patch("src.core.db_tools.DbFormatter.select_fields_from_db_model", return_value=TestData.report_drivers_desc_json)
def test_get_report_format_xml_order_desc(mock_select_dicts_from_db_model, client):
    response = client.get("/api/v1/report?order=desc&format=xml")
    expected = TestData.report_descending_drivers_xml
    assert response.status_code == 200
    combined_assertions_xml(response, expected)
    mock_select_dicts_from_db_model.assert_called_once()


@patch("src.core.db_tools.DbFormatter.select_fields_from_db_model", return_value=TestData.drivers_asc_json)
def test_get_drivers_without_args(mock_select_dicts_from_db_model, client):
    response = client.get("/api/v1/drivers/")
    expected = TestData.drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)
    mock_select_dicts_from_db_model.assert_called_once()


@patch("src.core.db_tools.DbFormatter.select_fields_from_db_model", return_value=TestData.drivers_asc_json)
def test_get_drivers_format_json_order_asc(mock_select_dicts_from_db_model, client):
    response = client.get("/api/v1/drivers/?order=asc&format=json")
    expected = TestData.drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)
    mock_select_dicts_from_db_model.assert_called_once()


@patch("src.core.db_tools.DbFormatter.select_fields_from_db_model", return_value=TestData.drivers_desc_json)
def test_get_drivers_format_xml_order_desc(mock_select_dicts_from_db_model, client):
    response = client.get("/api/v1/drivers/?order=desc&format=xml")
    expected = TestData.drivers_desc_xml
    assert response.status_code == 200
    combined_assertions_xml(response, expected)
    mock_select_dicts_from_db_model.assert_called_once()


@patch("src.core.db_tools.DbFormatter.get_driver_by_id", return_value=TestData.detail_driver_json)
def test_get_driver_without_args_positive(mock_get_driver_by_id, client):
    driver_id = TestData.driver_id
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}")
    expected = TestData.detail_driver_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)
    mock_get_driver_by_id.assert_called_once()


@patch("src.core.db_tools.DbFormatter.get_driver_by_id", return_value=TestData.detail_driver_json)
def test_get_driver_format_json_positive(mock_get_driver_by_id, client):
    driver_id = TestData.driver_id
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}?format=json")
    expected = TestData.detail_driver_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)
    mock_get_driver_by_id.assert_called_once()


@patch("src.core.db_tools.DbFormatter.get_driver_by_id", return_value=TestData.detail_driver_json)
def test_get_driver_format_xml_positive(mock_get_driver_by_id, client):
    driver_id = TestData.driver_id
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}?format=xml")
    expected = TestData.detail_driver_xml
    assert response.status_code == 200
    combined_assertions_xml(response, expected)
    mock_get_driver_by_id.assert_called_once()


@patch("src.core.db_tools.DbFormatter.get_driver_by_id", return_value=None)
def test_get_driver_not_exist_in_db_negative(mock_get_driver_by_id, client):
    driver_id = TestData.driver_id
    expected = {"message": f"Driver with driver_id: {driver_id} not found"}
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}")
    assert response.status_code == 404
    combined_assertions_json(response, expected)
    mock_get_driver_by_id.assert_called_once()


def test_page_not_found(client):
    expected = "404 NOT FOUND"
    response = client.get("/test_path")
    assert response.status_code == 404
    assert response.status == expected
