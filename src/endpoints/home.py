from flask import Blueprint, render_template

from src.helpers.api_helper import CustomError

home_endpoint = Blueprint('home_endpoint', __name__)


@home_endpoint.route("/")
def home_get():
    try:
        return render_template('home_api.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)