from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from src.api.v1.endpoints import Driver, Report, Drivers
from src.config import config, Config
from src.db.database import db


def create_app(env: Config):
    # app
    app_config = config[env.value]
    app = Flask(__name__)
    app.config.from_object(app_config)

    # db init
    db.init(app_config.SQLITE_DATABASE_URI)

    # api
    api = Api(app, prefix="/api/v1")
    api.add_resource(Report, "/report")
    api.add_resource(Drivers, "/drivers/")
    api.add_resource(Driver, "/drivers/driver_id=<string:driver_id>")

    # swagger
    Swagger(app)

    return app
