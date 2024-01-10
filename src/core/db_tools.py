from typing import List, Type

from peewee import Model
from playhouse.shortcuts import model_to_dict

from src.constants import OrderEnum


class DbFormatter:
    @staticmethod
    def select_fields_from_db_model(
        model_class: Type[Model],
        fields: List[str] | None = None,
        order: OrderEnum | None = None,
    ) -> List[dict]:
        """Get data from DB order by ASC or DESC, select only specified fields"""
        if not fields:
            query = model_class.select()
        else:
            fields_to_select = [getattr(model_class, field) for field in fields]
            query = model_class.select(*fields_to_select)

        if order:
            if OrderEnum(order) == OrderEnum.desc:
                query = query.order_by(model_class.id.desc())
            else:
                query = query.order_by(model_class.id.asc())
        return list(query.dicts())

    @staticmethod
    def get_driver_by_id(model: Type[Model], driver_id: str) -> dict:
        """Get driver data from DB by driver_id"""
        validate_driver_id = driver_id.strip().upper()
        driver = model.get_or_none(driver_id=validate_driver_id)
        return model_to_dict(driver) if driver else {}
