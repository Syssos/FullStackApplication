#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Settings Views

"""

# Related third party imports
from flask import jsonify, make_response, request, session
from flask_login import login_required, current_user

# Local application/library specific imports
from api.v1.views import app_views
import models

@app_views.route('/settings/view', methods=['GET'], strict_slashes=False)
@login_required
def return_user_settings():
    """ Return set of user specific data relating to "settings"
    """
    settings = models.storage.get("User", current_user.id).to_dict()
    Data = {
        "Username": settings["Username"],
        "ProfilePicture": settings["ProfilePicture"],
        "Email": settings["Email"],
    }

    return jsonify(Data)


@app_views.route('/settings/modify', methods=['POST'], strict_slashes=False)
@login_required
def return_modify_settings():
    """ Return set of user specific data relating to "settings"
    """
    content = request.get_json()
    user = models.storage.get("User", current_user.id)
    allUsers = models.storage.all("User")

    if "username" in content:
        if content["username"] != current_user.Username and content["username"] != "":
            for key, usr in allUsers.items():
                check = usr.to_dict()
                if check["Username"] == content["username"]:
                    return (jsonify({"status": "Username Exists Error"}))

            cart = models.storage.get("Cart", current_user.Cart)
            cart.User = content["username"]
            user.Username = content["username"]

            models.storage.update(user)
            models.storage.update(cart)

    if "profilepicture" in content:
        if content["profilepicture"] != current_user.ProfilePicture and content["profilepicture"] != "":
            user.ProfilePicture = content["profilepicture"]            
            models.storage.update(user)

    if "email" in content:
        if content["email"] != current_user.Email and content["email"] != "":
            for key, usr in allUsers.items():
                check = usr.to_dict()
                if check["Email"] == content["email"]:
                    return (jsonify({"status": "Email in use"}))

            user.Email = content["email"]
            models.storage.update(user)

    models.storage.save()
    return jsonify({"status": "OK"})