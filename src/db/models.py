from peewee import CharField, IntegerField, Model

from src.db.database import db


class BaseDriverModel(Model):
    driver_id = CharField()
    name = CharField()

    class Meta:
        database = db


class DetailDriver(BaseDriverModel):
    car = CharField()
    finish_time = CharField()
    start_time = CharField()
    lap_time = CharField()


class ReportDriver(BaseDriverModel):
    position = IntegerField()
    car = CharField()
    lap_time = CharField()


db_tables_list = [ReportDriver, DetailDriver]
