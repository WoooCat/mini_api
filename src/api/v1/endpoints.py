import logging
from functools import wraps
from typing import Callable, List, Union

from flasgger import swag_from

from flask import Response, abort, request
from flask_restful import Resource

from src.constants import XML_HEADER, FormatEnum
from src.core.converter import Converter
from src.core.db_tools import DbFormatter
from src.db.models import DetailDriver, ReportDriver


logger = logging.getLogger(__name__)


def response_format_decorator(func: Callable[..., Union[str, dict, List[dict]]]):
    """Set response format type decorator"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        data_response = func(*args, **kwargs)
        format_type = request.args.get("format")
        if format_type:
            format_enum = FormatEnum(format_type)
            if format_enum == FormatEnum.xml:
                return Response(data_response, content_type=XML_HEADER)
        return data_response

    return decorated_function


class Driver(Resource):
    @response_format_decorator
    @swag_from("./swagger_config/driver.yaml")
    def get(self, driver_id: str) -> Union[str, dict]:
        """Get Driver in JSON or XML format"""
        format_type = request.args.get("format")
        driver = DbFormatter.get_driver_by_id(DetailDriver, driver_id)
        if not driver:
            return abort(404, "Driver with driver_id: {} not found".format(driver_id))
        return Converter.convert_data_to_format(driver, format_type=format_type)


class Drivers(Resource):
    @response_format_decorator
    @swag_from("./swagger_config/drivers.yaml")
    def get(self) -> Union[str, dict, List[dict]]:
        """Get all Drivers sorted by descending or ascending have JSON or XML format"""
        order = request.args.get("order")
        format_type = request.args.get("format")
        sorted_drivers = DbFormatter.select_fields_from_db_model(
            DetailDriver, fields=["id", "driver_id", "name"], order=order
        )
        return Converter.convert_data_to_format(sorted_drivers, format_type=format_type)


class Report(Resource):
    @response_format_decorator
    @swag_from("./swagger_config/report.yaml")
    def get(self) -> Union[str, List[dict]]:
        """Get Common Drivers Statistic sorted by descending or ascending have JSON or XML format"""
        order = request.args.get("order")
        convert_type = request.args.get("format")
        sorted_drivers = DbFormatter.select_fields_from_db_model(ReportDriver, order=order)
        return Converter.convert_data_to_format(sorted_drivers, format_type=convert_type)
