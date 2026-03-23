from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

from app import views
