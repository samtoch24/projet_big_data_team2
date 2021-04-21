from flask import Blueprint

home_endpoint = Blueprint('home_endpoint', __name__)


@home_endpoint.route("/")
def home_get():
    return "Bienvenue sur notre API"