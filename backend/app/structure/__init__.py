from flask import Blueprint

blueprint = Blueprint(
    'structure_blueprint',
    __name__,
    url_prefix='/structure',
    template_folder='templates',
    static_folder='static'
)