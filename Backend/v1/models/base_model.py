#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus Base Product Object Model

BaseModel is responsible for essential methods and values
utilized by all product identifing classes, and will be
inheritaded by each. Values for each attribute can be 
assigned at the time of creation for both BaseModel and
child classes. Definitions of BaseModel class attributes
can be found below.

SKU - String, Unique identifier for each class instance (product)
ProductName - String, The name of the product the instance is representing
ProductImage - String, The URL for an image of the product, with a max length of 160 characters
ProductDescription - String, The description of the product, with a max of 250 characters
Price - Int, The price of the item before state and federal taxes(only important if tax calculater is added to the project)
Amount - Int, Quantity of in stock items of this type
Platform - String, Used to classify items for "Desktops", "Laptops", or "Other".

BaseModel is designed work with SQLalchemy, meaning classes 
inheriting from BaseModel, that follow the proper SQLacchemy
schemes, can be utilized to store oibjects directly into 
databases. This will be acheived in conjunction the database
engine for this project.
"""

# Standard library imports
from os import getenv

# Related third party imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

# Base is inherited at the same time as BaseModel, While not used in this file, it is used elsewhere and recommended to not be removed.
Base = declarative_base()

class BaseModel:
    # Attribute deffinition is required for future database use, check this backends README.md for more details
    SKU = Column(String(60), nullable=False, primary_key=True)
    ProductName = Column(String(60))
    ProductImage = Column(String(160))
    ProductDescription = Column(String(250))
    Price = Column(Integer())
    Amount = Column(Integer())
    Platform = Column(String(60))

    def __init__(self, *args, **kwargs):
        if (len(kwargs) == 0):
            # Default values, SKU randomization function method/function should be used to prevent errors with SKU being Unique
            self.SKU = "AVAAAAAA"
            self.ProductName = ""
            self.ProductImage = ""
            self.ProductDescription = ""
            self.Price = 0
            self.Amount = 0
            self.Platform = "Other"
        else:
            # SKU
            if kwargs.get("SKU"):
                self.SKU = kwargs["SKU"]
            else:
                self.SKU = 0
            # ProductName
            if kwargs.get("ProductName"):
                self.ProductName = kwargs["ProductName"]
            else:
                self.ProductName = 0
            # ProductImage
            if kwargs.get("ProductImage"):
                self.ProductImage = kwargs["ProductImage"]
            else:
                self.ProductImage = 0
            # ProductDescription
            if kwargs.get("ProductDescription"):
                self.ProductDescription = kwargs["ProductDescription"]
            else:
                self.ProductDescription = 0
            # Price
            if kwargs.get("Price"):
                self.Price = kwargs["Price"]
            else:
                self.Price = 0
            # Amount
            if kwargs.get("Amount"):
                self.Amount = kwargs["Amount"]
            else:
                self.Amount = 0
            # Platform
            if kwargs.get("Platform"):
                self.Platform = kwargs["Platform"]
            else:
                self.Platform = 0            

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """ Return: ex. [Ram] (AVAAAAAA) {atr: data, atr: data, atr: data, ...}
            The isolated data at the begining of the string is cnsidered to be of the most value. 
            The SKU is a unique Identifier and the class will identify the type of product
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.SKU, self.__dict__))

    def __repr__(self):
        """ Return: ex. [Ram] (AVAAAAAA) {atr: data, atr: data, atr: data, ...}
            The isolated data at the begining of the string is cnsidered to be of the most value. 
            The SKU is a unique Identifier and the class will identify the type of product
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.SKU, self.__dict__))

    def to_dict(self):
        """ Returns dictionary representation of BaseModel or class inheriting the BaseModel class.
            _sa_instance_state is removed from the dictionary if the attribute is present.
        """
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        if hasattr(self, "_sa_instance_state"):
            del cp_dct["_sa_instance_state"]
        return (cp_dct)
    