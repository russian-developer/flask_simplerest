from decimal import Decimal, InvalidOperation
from json import loads, dumps
from exceptions import ExceptionFieldValidation


class BaseField(object):
    def __init__(self, required=False, default=None):
        self.default = default
        self.required = required

    def to_python(self, value):
        raise NotImplementedError

    def from_python(self, value):
        raise NotImplementedError

class String(BaseField):
    def to_python(self, value):
        return unicode(value)

    def from_python(self, value):
        return unicode(value)

class List(BaseField):
    def to_python(self, value):
        _list = loads(value)
        if isinstance(_list, list):
            raise ExceptionFieldValidation(self.field_name)
        return _list

    def from_python(self, value):
        if isinstance(value, list):
            raise ExceptionFieldValidation(self.field_name, 'Outgoing variables must be list types')
        return value.__repr__()

class Dict(BaseField):
    def to_python(self, value):
        _dict = loads(value)
        if isinstance(_dict, dict):
            raise ExceptionFieldValidation(self.field_name)
        return _dict

    def from_python(self, value):
        if isinstance(value, dict):
            raise ExceptionFieldValidation(self.field_name, 'Outgoing variables must be dict types')
        return value.__repr__()

class Integer(BaseField):
    def to_python(self, value):
        try:
            return int(value)
        except ValueError:
            raise ExceptionFieldValidation(self.field_name)
    from_python = to_python


class Deciaml(BaseField):
    def to_python(self, value):
        try:
            return Deciaml(value)
        except InvalidOperation:
            raise ExceptionFieldValidation(self.field_name)

    def from_python(self, value):
        return unicode(value)

class Float(BaseField):
    def to_python(self, value):
        try:
            return float(value)
        except ValueError:
            raise ExceptionFieldValidation(self.field_name)

    def from_python(self, value):
        return unicode(value)

class File(BaseField): pass
class Image(File): pass
