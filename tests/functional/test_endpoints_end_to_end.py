from tests.precondition_data import TestData
from tests.utils import combined_assertions_json, combined_assertions_xml


def test_get_report_without_args(test_database, client):
    expected = TestData.report_drivers_asc_json
    response = client.get("/api/v1/report")
    assert response.status_code == 200
    combined_assertions_json(response, expected)


def test_get_report_format_json_order_asc(test_database, client):
    response = client.get("/api/v1/report?order=asc&format=json")
    expected = TestData.report_drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected)


def test_get_report_format_xml_order_desc(test_database, client):
    response = client.get("/api/v1/report?order=desc&format=xml")
    expected = TestData.report_drivers_desc_xml
    assert response.status_code == 200
    combined_assertions_xml(response, expected)


def test_get_drivers_without_args(test_database, client):
    response = client.get("/api/v1/drivers/")
    expected_data = TestData.drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected_data)


def test_get_drivers_order_acs_format_json(test_database, client):
    response = client.get(f"/api/v1/drivers/?order=asc&format=json")
    expected_data = TestData.drivers_asc_json
    assert response.status_code == 200
    combined_assertions_json(response, expected_data)


def test_get_drivers_order_desc_format_xml(test_database, client):
    response = client.get(f"/api/v1/drivers/?order=desc&format=xml")
    expected_data = TestData.drivers_desc_xml
    assert response.status_code == 200
    combined_assertions_xml(response, expected_data)


def test_get_driver_without_args(test_database, client):
    driver_id = TestData.driver_id
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}")
    expected_data = TestData.detail_driver_json
    assert response.status_code == 200
    combined_assertions_json(response, expected_data)


def test_get_driver_format_json(test_database, client):
    driver_id = TestData.driver_id
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}?format=json")
    expected_data = TestData.detail_driver_json
    assert response.status_code == 200
    combined_assertions_json(response, expected_data)


def test_get_driver_format_xml(test_database, client):
    driver_id = TestData.driver_id
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}?format=xml")
    expected_data = TestData.detail_driver_xml
    assert response.status_code == 200
    combined_assertions_xml(response, expected_data)


def test_get_driver_not_exist_negative(test_database, client):
    driver_id = "not_exist_driver_id"
    expected_message = {"message": f"Driver with driver_id: {driver_id} not found"}
    response = client.get(f"/api/v1/drivers/driver_id={driver_id}")
    assert response.status_code == 404
    combined_assertions_json(response, expected_message)
