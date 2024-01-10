from typing import List, Tuple

from reportracing import Driver, build_report, sort_report_data

from src.constants import OrderEnum


class MyReportRacing:
    """Additional extra logic for Reportracing package"""

    def __init__(self, path):
        self.path = path
        self.report_data = build_report(path)

    def get_drivers(self, order: str = None) -> List[Tuple[int, Driver]]:
        """Get Drivers with positions"""
        if order:
            if OrderEnum(order) == OrderEnum.desc:
                return self.add_drivers_position(self.report_data, reverse=True)
        return self.add_drivers_position(self.report_data)

    @staticmethod
    def add_drivers_position(driver_data: List[Driver], reverse: bool = False) -> List[Tuple[int, Driver]]:
        """Add Drivers position to list of Drivers"""
        drivers_with_position = [(pos, driver) for pos, driver in enumerate(sort_report_data(driver_data), start=1)]
        if reverse:
            return list(reversed(drivers_with_position))
        return drivers_with_position
