#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Cart Views

"""

# Related third party imports
from flask import jsonify, make_response, request, session
from flask_login import login_required, current_user

# Local application/library specific imports
from api.v1.views import app_views
import models

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
        newData["Items"].append(models.storage.getBySKU(item).to_dict())

    return jsonify(newData)

@app_views.route('/cart/add', methods=['POST'], strict_slashes=False)
@login_required
def add_cart_item():
    """ Adds an item to users cart
    """
    content = request.get_json()
    cart = models.storage.get("Cart", current_user.Cart)
    desiredAmount = 1
    newData = {
        "Items": [],
        "updated_at": cart.updated_at
    }

    if "item" in content:
        item = models.storage.getBySKU(content["item"])

        if "quantity" in content:
            desiredAmount = content["quantity"]

        if desiredAmount <= item.Amount:
            item.Amount = item.Amount - desiredAmount
            models.storage.update(item)
            models.storage.save()
        else:
            return jsonify({"error":"quantity"})
        
        cart.Items.append(item.SKU)
        models.storage.save()

        for item in cart.Items:
            newData["Items"].append(models.storage.getBySKU(item).to_dict())
        
        return jsonify(newData)
    else:
        return jsonify({"error":"item"})

@app_views.route('/cart/remove', methods=['POST'], strict_slashes=False)
@login_required
def remove_cart_item():
    """ Removes an item from the users cart
    """
    
    content = request.get_json()
    cart = models.storage.get("Cart", current_user.Cart)
    
    newData = {
        "Items": [],
        "updated_at": cart.updated_at
    }

    if "item" in content:
        item = models.storage.getBySKU(content["item"])
      
        if item.SKU in cart.Items:
            cart.Items.remove(item.SKU)
            item.Amount = item.Amount + 1
            models.storage.update(item)
            models.storage.update(cart)
            models.storage.save()

        for cartItem in cart.Items:
            newData["Items"].append(models.storage.getBySKU(cartItem).to_dict())
        
        return jsonify(newData)
    else:
        return jsonify({"error":"item"})