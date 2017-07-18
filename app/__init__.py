from flask import Flask

#initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config files
app.config.from_object('config')
