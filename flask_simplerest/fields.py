class BaseField(object):
    def __init__(self, required=False, default=None):
        self.default = default
        self.required = required

    def to_python(self, value):
        return value

    def from_python(self, value):
        return value

class String(BaseField): pass
class List(BaseField): pass
class Dict(BaseField): pass
class Integer(BaseField): pass
class Deciaml(BaseField): pass
class Float(BaseField): pass
class File(BaseField): pass
class Image(File): pass