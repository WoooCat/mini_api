from typing import List, Tuple, Union
from xml.dom.minidom import parseString

from dicttoxml import dicttoxml
from reportracing import Driver

from src.db.drivers_classes import DetailedDriver, ReportDriver


class Converter:
    @classmethod
    def formatting_data(cls, format_type: str, report_data: Union[dict, List[dict]]) -> Union[dict, str]:
        """Change format type response data [ JSON, XML ]"""
        if format_type == "xml":
            return cls.driver_to_xml(report_data)
        return report_data

    @staticmethod
    def create_report_driver_dict(enum_driver: Tuple[int, Driver]) -> dict:
        """Create dict for report endpoints"""
        id_, driver = enum_driver
        driver = ReportDriver(
            id=id_,
            driver_id=str(driver.abbreviation),
            name=driver.name,
            position=id_,
            car=driver.car,
            lap_time=str(driver.best_time),
        )
        return driver.__dict__

    @staticmethod
    def create_detailed_driver_dict(enum_driver: Tuple[int, Driver]) -> dict:
        """Create dict for report endpoints"""
        id_, driver = enum_driver
        driver = DetailedDriver(
            id=id_,
            driver_id=str(driver.abbreviation),
            name=driver.name,
            car=driver.car,
            lap_time=str(driver.best_time),
            start_time=str(driver.start_time),
            finish_time=str(driver.finish_time),
        )
        return driver.__dict__

    @staticmethod
    def driver_to_xml(driver_dict: Union[dict, List[dict]]) -> str:
        """Convert Drivers dictionary to XML format"""
        xml = dicttoxml(driver_dict, attr_type=False)
        formatted_xml = parseString(xml)
        return formatted_xml.toprettyxml()

    @staticmethod
    def convert_data_to_format(drivers_data: Union[dict, List[dict]], format_type: str) -> Union[str, dict, List[dict]]:
        """Get info about Drivers in XML or JSON formats for report end drivers endpoints"""
        return Converter.formatting_data(format_type, drivers_data)
