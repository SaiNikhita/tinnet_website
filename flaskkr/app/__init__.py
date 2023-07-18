from flask import Flask, url_for
from importlib import import_module
from structure import dash_app
from os import path

def register_blueprints(app):
    for module_name in ('base', 'structure'):
        module = import_module('app.{}.routes'.format(module_name))
        print(module.blueprint)
        app.register_blueprint(module.blueprint)
        a = [str(p) for p in app.url_map.iter_rules()]
        print(a)

def create_app():
    app = Flask(__name__, static_folder='base/static')
    register_blueprints(app)
    app = dash_app.Add_Dash(app)
    return app

