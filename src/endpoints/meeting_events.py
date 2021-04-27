from flask import Blueprint, render_template

from src.helpers.api_helper import CustomError

meeting_events_endpoint = Blueprint('meeting_events_endpoint', __name__)


@meeting_events_endpoint.route("/")
def meeting_events_get():
    try:
        return render_template('meeting_events.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)


