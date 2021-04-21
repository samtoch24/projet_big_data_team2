from flask import Blueprint, render_template

docs_endpoint = Blueprint('docs_endpoint', __name__)


@docs_endpoint.route("/")
def docs_get():
    return render_template('swaggerui.html')