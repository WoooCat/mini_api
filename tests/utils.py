def combined_assertions_json(response, expected):
    """Combine asserts for JSON Header"""
    expected_json_header = "application/json"
    actual_result = response.json
    assert response.headers["Content-Type"] == expected_json_header
    assert actual_result == expected


def combined_assertions_xml(response, expected):
    """Combine asserts for XML Header"""
    expected_xml_header = "text/xml; charset=utf-8"
    actual_result = response.text
    assert response.headers["Content-Type"] == expected_xml_header
    assert actual_result == expected
