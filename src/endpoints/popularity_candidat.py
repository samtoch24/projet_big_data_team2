from flask import Blueprint, render_template

from src.collectors.collectors_ppopularity import popularity_on_media_pdf
from src.helpers.api_helper import CustomError

popularity_candidat_endpoint = Blueprint('popularity_candidat_endpoint', __name__)


@popularity_candidat_endpoint.route("/")
def docs_get():
    try:
        return render_template('popularity_candidat.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)


@popularity_candidat_endpoint.route("/csv_file/latest/download/")
def popularity_candidat_csv_file_latest_download_get():
    return popularity_on_media_pdf()
    """ télécharge le dernier fichier des données de la tendance des votes """
    # try:
    #     return render_template('daily_vote_trend_success.html')
    # except:
    #     return CustomError("GET error", 400).throw()
    # else:
    #     return json.dumps(result, indent=4)


@popularity_candidat_endpoint.route("/analysis-elections/daily-vote/")
def vote_tendancy_analysis_elections_daily_vote_get():
    """ analyse le fichier file_name de ma source """
    try:
        return render_template('daily_vote_trend.html')
    except:
        return CustomError("GET error", 400).throw()
    else:
        return json.dumps(result, indent=4)
