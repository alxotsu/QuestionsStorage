from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

__all__ = ['app', 'db', 'Config']


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
