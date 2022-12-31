from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# Create the Flask app
app = Flask(__name__)
CORS(app)
# Load the configuration from the instance folder
app.config.from_pyfile("../instance/config.py")

# Create a SQLAlchemy object
db = SQLAlchemy(app)

# Import the routes and models modules
from app import routes,models

with app.app_context():
    db.create_all()