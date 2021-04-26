
from flask import Blueprint
from src.collectors.collectors_pop import popularity_latest_download

popularity_endpoint = Blueprint('popularity_endpoint', __name__)


@popularity_endpoint.route("/csv_file/latest/download/")
def popularity_csv_file_latest_download_get():
    popularity_latest_download()
    """ télécharge le dernier fichier des données de popularité des candidats """

#
# @popularity_endpoint.route("/ma_source_1/latest/download")
# def covid_ma_source_1_latest_download_get():
#     """ télécharge le dernier fichier de ma source 1 """
#
#
# @popularity_endpoint.route("/ma_source_2/<string:file_name>/download")
# def covid_ma_source_2_latest_download_get(file_name):
#     """ télécharge le fichier file_name de ma source 2 """
#
#
# @popularity_endpoint.route("/ma_source_3")
# def covid_ma_source_3_get():
#     """ retourne les données de ma source 3 """
