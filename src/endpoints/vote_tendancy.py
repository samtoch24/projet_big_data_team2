from flask import Blueprint, render_template

from src.collectors.collectors_tendancy_vote import vote_tendancy_latest_download
from src.helpers.api_helper import CustomError

vote_tendancy_endpoint = Blueprint('vote_tendancy_endpoint', __name__)


@vote_tendancy_endpoint.route("/")
def docs_get():
    try:
        return render_template('daily_vote_trend.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)


@vote_tendancy_endpoint.route("/docs/#/tendancy_votes/getInventory")
def vote_tendancy_docs_tendancy_votes_getInventory_get():
    return vote_tendancy_latest_download()
    """ télécharge le dernier fichier des données de la tendance des votes """
    # try:
    #     return render_template('daily_vote_trend_success.html')
    # except:
    #     return CustomError("GET error", 400).throw()
    # else:
    #     return json.dumps(result, indent=4)


@vote_tendancy_endpoint.route("/docs/#/tendancy_votes/getInventory/analysis")
def vote_tendancy_docs_tendancy_votes_getInventory_analysis_get():
    """ analyse le fichier file_name de ma source """
    try:
        return render_template('daily_vote_trend.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)
