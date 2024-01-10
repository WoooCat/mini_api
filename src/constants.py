from enum import Enum


XML_HEADER = "text/xml; charset=utf-8"
JSON_HEADER = "application/json; charset=utf-8"


class FormatEnum(str, Enum):
    xml = "xml"
    json = "json"


class OrderEnum(str, Enum):
    desc = "desc"
    asc = "asc"
