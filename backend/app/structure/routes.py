from . import blueprint
from flask import render_template
from structure import dash_app

@blueprint.route('/structure/1')
def structure_template():
    return render_template('structure.html', dash_url = dash_app.url_base)
