import random
import string
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

from reportracing import Driver, sort_report_data
from src.core.converter import Converter
from src.core.proxy_interface import MyReportRacing
from src.db.drivers_classes import BaseDriver


@dataclass
class TestDriver:
    """Object for initialisation Test Driver"""

    id: int
    abbreviation: str
    name: str
    car: str
    start_time: datetime
    finish_time: datetime
    best_time: timedelta


class PreconditionData:
    """Class for create precondition data"""

    def create_random_driver(self) -> TestDriver:
        """Create random Driver"""
        abbr = self.generate_random_str(3)
        id_ = random.randint(1, 100)
        name = self.generate_random_str(random.randint(3, 20))
        car = self.generate_random_str(random.randint(3, 20))
        offset = random.randint(60, 80)
        start_time_ = time.time()
        finish_time_ = start_time_ + offset
        start_datetime = datetime.fromtimestamp(start_time_)
        finish_datetime = datetime.fromtimestamp(finish_time_)
        best_timedelta = finish_datetime - start_datetime

        driver = TestDriver(
            id=id_,
            abbreviation=abbr,
            name=name,
            car=car,
            start_time=start_datetime,
            finish_time=finish_datetime,
            best_time=best_timedelta,
        )
        return driver

    def generate_random_drivers(self, count) -> List[TestDriver]:
        """Generate list of random Drivers"""
        return [self.create_random_driver() for _ in range(count)]

    @staticmethod
    def generate_random_str(length):
        """Generate random string"""
        letters_and_digits = string.ascii_uppercase + string.digits
        return "".join(random.choices(letters_and_digits, k=length))

    @staticmethod
    def create_base_driver_dict(enum_driver: Tuple[int, Driver]) -> dict:
        """Convert Driver to JSON"""
        position, driver = enum_driver
        driver = BaseDriver(id=position, driver_id=str(driver.abbreviation), name=driver.name)
        return driver.__dict__


class TestData:
    """Init Precondition Data"""

    precondition = PreconditionData()
    drivers = precondition.generate_random_drivers(19)

    drivers_sorted = sort_report_data(drivers)
    enum_drivers_ascending = MyReportRacing.add_drivers_position(drivers_sorted)
    enum_drivers_descending = MyReportRacing.add_drivers_position(drivers_sorted, reverse=True)

    driver_with_position = (1, drivers_sorted[0])
    driver_id = drivers_sorted[0].abbreviation

    list_of_drivers_dict_report = list(map(Converter.create_report_driver_dict, enum_drivers_ascending))
    list_of_drivers_xml_report = Converter.driver_to_xml(list_of_drivers_dict_report)

    drivers_asc_json = [PreconditionData.create_base_driver_dict(driver) for driver in enum_drivers_ascending]
    drivers_desc_json = [PreconditionData.create_base_driver_dict(driver) for driver in enum_drivers_descending]
    drivers_desc_xml = Converter.driver_to_xml(drivers_desc_json)

    report_drivers_asc_json = [Converter.create_report_driver_dict(driver) for driver in enum_drivers_ascending]
    report_drivers_desc_json = [Converter.create_report_driver_dict(driver) for driver in enum_drivers_descending]

    report_drivers_desc_xml = Converter.driver_to_xml(report_drivers_desc_json)
    detail_driver_json = Converter.create_detailed_driver_dict(driver_with_position)
    detail_driver_xml = Converter.driver_to_xml(detail_driver_json)
    report_driver_json = Converter.create_report_driver_dict(driver_with_position)

    report_descending_drivers_xml = Converter.convert_data_to_format(
        format_type="xml", drivers_data=report_drivers_desc_json
    )
