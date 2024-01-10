from logger_config import initialize_logger
from src.app import create_app
from src.config import Config

if __name__ == "__main__":
    initialize_logger()
    app = create_app(Config.development)
    app.run()
