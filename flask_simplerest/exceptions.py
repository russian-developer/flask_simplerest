from werkzeug.exceptions import HTTPException
import json

class ExceptionFieldNotFound(HTTPException):
    def __init__(self, required_fields, all_required_fields, all_fields):
        self.response = None
        _required_field = ', '.join(required_fields)
        _all_required_fields = ', '.join(all_required_fields)
        _all_fields = ', '.join(all_fields)
        self.description = 'Field "%s" not found, you must pass "%s", you can pass "%s"' % (
            _required_field,
            _all_required_fields,
            _all_fields
        )

    def get_body(self, environ=None):
        return json.dumps(dict(error=self.description))

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

class ExceptionFieldValidation(ExceptionFieldNotFound):
    def __init__(self, field, description=None):
        self.response = None
        self.description = 'Invalid data type for field "%s"' % field
        if description:
            self.description += ', "%s"' % description