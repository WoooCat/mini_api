from dataclasses import dataclass


@dataclass
class BaseDriver:
    id: int
    driver_id: str
    name: str


@dataclass
class DetailedDriver(BaseDriver):
    car: str
    finish_time: str
    start_time: str
    lap_time: str


@dataclass
class ReportDriver(BaseDriver):
    position: int
    car: str
    lap_time: str
