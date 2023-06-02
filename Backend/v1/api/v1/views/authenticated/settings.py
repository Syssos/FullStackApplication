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
            cart = models.storage.get("Cart", current_user.Cart)
            cart.User = content["username"]
            user.Username = content["username"]

            models.storage.update(user)
            models.storage.update(cart)
        else:
            # Username is the same, or unchanged
            pass

    if "profilepicture" in content:
        print(content["profilepicture"])
        if content["profilepicture"] != current_user.ProfilePicture and content["profilepicture"] != "":
            user.ProfilePicture = content["profilepicture"]            
            models.storage.update(user)
        else:
            # Profile Picture is the same, or unchanged
            pass

    if "email" in content:
        if content["email"] != current_user.Email and content["email"] != "":
            user.Email = content["email"]
            models.storage.update(user)
        else:
            # Email is the same, or unchanged
            pass

    models.storage.save()
    return jsonify({"status": "OK"})