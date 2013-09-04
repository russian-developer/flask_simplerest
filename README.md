Flask simple REST
=========================

A Flask extansion for simple ReSTful api generation

Install
-------

For install you can use pip:
```
pip install flask_simplerest
```

Usage
-------

app.py
```
from flask import Flask
from flask.ext.simplerest import SimpleRestApp
from handlers.myhandler import MyHandler

app = Flask(__name__)
rest = SimpleRestApp(app)

MyHandler(rest, 'prefix_if_needed')

@rest('/index', 'PUT')
def some_put_method():
    pass

app.run()
```

handlers/myhandler.py
```
from flask.ext.simplerest import SimpleRestResource, rest
from flask.ext.simplerest import fields

class Projects(SimpleRestResource):
    @rest('/', 'POST')
    def test(self, name=fields.String):
        return {'name':name}

    @rest('/<int:my_id>/123', 'POST')
    def test2(self, my_id, name=fields.String(default='Costos')):
        return dict(my_id=my_id, name=name)

```

Bash
(first you must run application)
```
curl http://127.0.0.1:5000/ -d name=Murza
{
    'name': 'Murza'
}
```

