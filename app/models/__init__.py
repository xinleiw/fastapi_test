import json
from datetime import datetime

ATTR_NAMES_FOR_JSON_FORMAT_CONVERSION = ["raw_meta", "tags"]


class ModelMixin(object):
    @property
    def to_dict(self):
        rt = {}
        if hasattr(self, "__table__"):
            for c in self.__table__.columns:
                value = getattr(self, c.name)
                if type(value) == datetime:
                    value = value.strftime("%Y-%m-%d %H:%M:%S")
                elif c.name in ATTR_NAMES_FOR_JSON_FORMAT_CONVERSION:
                    value = json.loads(value)
                else:
                    pass
                rt[c.name] = value
        return rt

    def copy_from_dict(self, d):
        if hasattr(self, "__table__"):
            for c in self.__table__.columns:
                value = d.get(c.name)
                if value is not None:
                    if c.name in ATTR_NAMES_FOR_JSON_FORMAT_CONVERSION:
                        value = json.dumps(value)
                    setattr(self, c.name, value)

    def __repr__(self):
        return repr(self.to_dict)
