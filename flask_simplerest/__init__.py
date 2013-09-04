from flask import jsonify, request
from exceptions import ExceptionFieldNotFound
import inspect

class SimpleRestApp(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, path, method):
        def wrapper(fn):
            fn_inspect = inspect.getargspec(fn)
            fields = dict()
            if fn_inspect.defaults:
                fields.update(zip(fn_inspect.args[-len(fn_inspect.defaults):], fn_inspect.defaults))

            def output(*a, **k):
                data = {}
                fields_that_are_not = []
                _required_fields = []
                _not_required_fields = []

                for key, value in fields.items():
                    if isinstance(value, type):
                        value = value()
                    if value.required:
                        _required_fields.append(key)
                    else:
                        _not_required_fields.append(key)
                    if not request.form.has_key(key) and not value.default: fields_that_are_not.append(key)
                    data[key] = value.to_python(request.form.get(key, value.default))
                if fields_that_are_not:
                    raise ExceptionFieldNotFound(fields_that_are_not, _required_fields, fields)
                if request.view_args:
                    data.update(request.view_args)
                result = fn(**data)
                if isinstance(result, dict):
                    return jsonify(result)
                return ''
            output.__name__ = fn.__name__
            return self.app.route(path, methods=[method])(output)
        return wrapper


class SimpleRestResource(object):
    def __init__(self, rest_instance, prefix=''):
        for method_name, instance in inspect.getmembers(self):
            if method_name.startswith('__'):
                continue
            if not hasattr(instance, 'path') or not hasattr(instance, 'method'):
                raise Exception('You must use @rest(path, method) for all method of your cls')
            setattr(self, method_name, rest_instance(prefix + instance.path, instance.method)(instance))

def rest(path, method):
    def wrapper(fn):
        fn.path = path
        fn.method = method
        return fn
    return wrapper