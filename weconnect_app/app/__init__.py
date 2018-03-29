from flask import Flask, session
from config import config
from flasgger import Swagger
# variables to store data in memory
users = list()
known_user_ids = list()
reviews = list()
known_review_ids = list()
businesses = list()
known_business_ids = list()
known_usernames = list()
SECRET_KEY = 'veryhardkey'

swagger = Swagger()


def create_app(config_name):
    # instantiate the application and packages required
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    swagger.init_app(app)
    # create blueprint of main
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # create blueprint of the api
    from .api_v_1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_ref='/api/v1/')
    return app
