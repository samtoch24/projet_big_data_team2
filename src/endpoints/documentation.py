from flask import Blueprint, render_template

from src.helpers.api_helper import CustomError

docs_endpoint = Blueprint('docs_endpoint', __name__)


@docs_endpoint.route("/")
def docs_get():
    try:
        return render_template('swaggerui.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)


