from flask import Blueprint, render_template

from src.helpers.api_helper import CustomError

position_candidat_endpoint = Blueprint('position_candidat_endpoint', __name__)


@position_candidat_endpoint.route("/")
def position_candidat_get():
    try:
        return render_template('position_candidat.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)


