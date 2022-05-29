import os
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)
app.config.from_file("config.json", load=json.load)

db = SQLAlchemy(app)

# Load models
from App.models.users import *

# Load routes
from App.routes.views import *
from App.routes.api   import *
