from flask import Flask
from flask_cors import CORS
from src.endpoints.popularity_latest_download import popularity_endpoint
from src.endpoints.documentation import docs_endpoint
from src.endpoints.home import home_endpoint

VERSION = '/v0.0.1'
app = Flask(__name__)

app.register_blueprint(home_endpoint, url_prefix=VERSION + '/home')
app.register_blueprint(docs_endpoint, url_prefix=VERSION + '/docs')
app.register_blueprint(popularity_endpoint, url_prefix=VERSION + '/popularity_candidats')
CORS(app)

if __name__ == '__main__':
 app.run('127.0.0.1', 5000)
