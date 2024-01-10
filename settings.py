import os


class Settings:
    """Views Configuration Class"""

    REPORT_DATA_PATH = os.environ.get("REPORT_DATA_PATH", "report_data")
    DB = os.environ.get("FLASK_API_DATABASE", "app.db")
    LOGGER_CONFIG_NAME = os.environ.get("LOGGER_CONFIG_FILE", "logging.conf")
