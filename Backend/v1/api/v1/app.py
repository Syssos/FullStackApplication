#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus API Version 1

"""

# Standard library imports
import os

# Related third party imports
from flask import Flask, Blueprint, jsonify
from flask import Flask
from flask_cors import CORS

# Local application/library specific imports
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/api/v1/*": {"origins": "*"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

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