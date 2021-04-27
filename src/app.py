from flask import Flask
from flask_cors import CORS
from src.endpoints.popularity_candidat import popularity_candidat_endpoint
from src.endpoints.popularity_latest_download import popularity_endpoint
from src.endpoints.documentation import docs_endpoint
from src.endpoints.position_candid import position_candidat_endpoint
from src.endpoints.meeting_events import meeting_events_endpoint
from src.endpoints.home import home_endpoint
from src.endpoints.vote_tendancy import vote_tendancy_endpoint

VERSION = '/v0.0.1'
app = Flask(__name__)

# @app.route("/v0.0.1/home/")
# def helloworl_get():
#   return ""

app.register_blueprint(home_endpoint, url_prefix=VERSION + '/home')
app.register_blueprint(vote_tendancy_endpoint, url_prefix=VERSION + '/home/daily-vote-tendancy')
app.register_blueprint(docs_endpoint, url_prefix=VERSION + '/docs')
app.register_blueprint(position_candidat_endpoint, url_prefix=VERSION + '/position-of-candidat')
app.register_blueprint(meeting_events_endpoint, url_prefix=VERSION + '/meeting_events')
app.register_blueprint(popularity_endpoint, url_prefix=VERSION + '/popularity_candidats')
app.register_blueprint(popularity_candidat_endpoint, url_prefix=VERSION + '/popularity-of-candidats')
CORS(app)

if __name__ == '__main__':
 app.run('127.0.0.1', 5000)