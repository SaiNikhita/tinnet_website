from flask import jsonify, render_template, redirect, request, url_for
from . import blueprint

@blueprint.route('/')
def route_default():
    return render_template('base.html')