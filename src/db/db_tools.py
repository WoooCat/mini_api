import logging

from logger_config import initialize_logger
from settings import Settings
from src.core.converter import Converter
from src.core.proxy_interface import MyReportRacing
from src.db.models import (
    DetailDriver,
    ReportDriver,
    db,
    db_tables_list,
    BaseDriverModel,
)


logger = logging.getLogger(__name__)
initialize_logger()


def to_create_tables() -> None:
    """Create the database.db tables if they don't exist."""
    logging.warning("Creating db tables...")
    db.init(Settings.DB)
    db.create_tables(db_tables_list, safe=True)
    logger.warning("Database tables created successfully!")


def to_insert_data(table_list: list) -> None:
    """Populate the specified tables with the data, skipping duplicates."""
    logging.warning("Inserting data into the db...")
    data = MyReportRacing(Settings.REPORT_DATA_PATH)
    enum_drivers = data.get_drivers()
    details_drivers = [Converter.create_detailed_driver_dict(driver) for driver in enum_drivers]
    report_drivers = [Converter.create_report_driver_dict(driver) for driver in enum_drivers]

    with db.atomic():
        for table in table_list:
            if not table.table_exists():
                logging.error(f"The table '{table.__name__}' does not exist.")
            else:
                table.truncate_table()
                if issubclass(table, BaseDriverModel):
                    if table == ReportDriver:
                        table.insert_many(report_drivers).execute()
                    elif table == DetailDriver:
                        table.insert_many(details_drivers).execute()
                    logger.warning(f"Data inserted into '{table.__name__}' successfully!")
                else:
                    logging.error(f"The table '{table.__name__}' does not inherit from BaseDriverModel.")
