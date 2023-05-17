#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Autherized Views

This file will be responsible for any route that requires authenitication
by the server. This includes things such as loging in, loging out, getting
user shopping carts, etc... 

Authentication, the Session, and any assosiated cookies are all handled through
the flask_login add-on. For more information see the link below
https://flask-login.readthedocs.io/en/latest/
"""

# Related third party imports
from flask import jsonify, make_response, request, session
from flask_login import login_user, login_required, current_user, logout_user

# Local application/library specific imports
from api.v1.views import app_views

import models

@app_views.route('/autherize', methods = ['POST', 'GET'])
def return_auth():
    """ Autherizes a user by checking their password. If password matches the session cookie is created "authenticating" the user.
    """
    if request.method == "POST":
        # record the user name
        data = request.get_json()
        print(data)
        user = data["username"]
        pwd = data["password"]
        users = models.storage.all("User")
        for key, value in users.items():
            if value.Username == user and value.Password == pwd:
                login_user(value)
                return jsonify({'login': 'success'})

    return jsonify({'login': 'failure'})

@app_views.route("/logout")
@login_required
def logout():
    """ Logs a user out be removing there active session
    """
    logout_user()
    return jsonify({'autherized': 'no'})

@app_views.route('/cart', methods=['GET'], strict_slashes=False)
@login_required
def return_cart():
    """ Displays cart items depending on user session
    """
    cart = models.storage.get("Cart", current_user.Cart).to_dict()
    newData = {
        "Items": [],
        "updated_at": cart["updated_at"]
    }

    for item in cart["Items"]:
        newData["Items"].append(models.storage.getBySKU(item))

    return jsonify(newData)

@app_views.route('/isauth', methods=['GET'], strict_slashes=False)
@login_required
def return_authstatus():
    """ 
    """
    return jsonify("authenticated")