#!/usr/bin/python3
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

cors = CORS(app, resources={"/*": {"origins": "127.0.0.1"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def return_homePage():
        ''' Returns api status
        '''

        return render_template('index.html')

@app.route('/browse')
def return_category():
        ''' Returns api status
        '''

        return render_template('browse.html')

@app.route('/view')
def return_item():
        ''' Returns api status
        '''

        return render_template('view.html')

@app.errorhandler(404)
def errorhandler(error):
    """ Returns status 404 Not found
    """
    return jsonify({'error': 'Not found'}), 404

if __name__ == "__main__":
    hosts = os.getenv("API_HOST", default="127.0.0.1")
    ports = int(os.getenv("API_PORT", default=5001))
    app.run(host=hosts, port=ports, threaded=True)