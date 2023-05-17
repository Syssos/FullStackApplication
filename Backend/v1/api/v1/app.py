#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus API Version 1

This file houses the initial API application starting point.
It defines the app views, cors, and handles errors such as
404 not found, adn the app teardown.

This file should not house any routes outside or error handling.
All routes should be defined within the the app views.
"""

# Standard library imports
import os

# Related third party imports
from flask import Flask, Blueprint, jsonify
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

# Local application/library specific imports
from api.v1.views import app_views
from models import storage
from models.user import User

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, supports_credentials=True, resources={"/api/v1/*": {"origins": "http://localhost:5001"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """ Loads user object for use with authentication
    """
    return User().get(user_id)

@app.teardown_appcontext
def teardown(self):
    """ calls close to close session
    """
    # Close reloads for know, function needs to be changed to commit changes to file storage
    storage.close()

@app.errorhandler(404)
def errorhandler(error):
    """ Returns status 404 Not found
    """
    return jsonify({'error': 'Not found'}), 404

if __name__ == "__main__":
    hosts = os.getenv("API_HOST", default="127.0.0.1")
    ports = int(os.getenv("API_PORT", default=5000))
    app.run(host=hosts, port=ports, threaded=True)