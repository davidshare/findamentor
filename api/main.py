import os
from flask import Flask
from flask_cli import FlaskCLI
from flask_migrate import Migrate

from config.utils import get_env_vars
from config.environment_config import config
from config.db import db

def create_app(config_override=None):
  '''
    function to create a flask application
    this utilizes the factory pattern

    :param config_override: Overide default configuration settings
    :returns app: Flask app
  '''

  app=Flask(__name__, instance_relative_config=True)
  default_config = os.getenv('FLASK_ENV', 'development')

  if config_override:
    app.config.from_object(config[config_override])
  else:
    app.config.from_object(config[default_config])

  return app

app = create_app(get_env_vars('FLASK_ENV'))

app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import api.models.users
Migrate(app, db)

@app.route('/')
def index():
    return "<h1>Welcome to Mentoria!!!</h1>"

FlaskCLI(app)
