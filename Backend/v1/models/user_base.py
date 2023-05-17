#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus  User Base Object Model

The UserBase class is simular to the BaseModel class in terms of use
through-out the application, however the main difference between the
two comes down to the context in which they are used. The UserBase
class should be utilized for objects not intended on being shared with
others, ie user information, a shopping cart, ownership of blogs posts 
on a forum, etc...

The attributes assigned to this class are minimal, and are intended on
being used for tracking purposes. These atributes should not be modified
by the inheriting class, excluding of course the "updated_at" attribute,
which should be modified each time the object is modified, ie a username
is changed, a item is added to a cart, etc...
"""

# Standard library imports
import uuid
from os import getenv
from datetime import datetime

# Related third party imports
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Local application/library specific imports
import models

# Base is inherited at the same time as BaseModel, While not used in this file, it is used elsewhere and recommended to not be removed.
Base = declarative_base()

class UserBase:
    # Attribute deffinition is required for future database use, check this backends README.md for more details
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialize public instance, assigns attributes and sets created_at time.
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("created_at"):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
            if not self.id:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """ Return string representation of UserBase class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """ Return string representation of UserBase class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ Updates the updated_at attribute with new datetime, then commits changes to file storage.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Return dictionary representation of User class.
        """
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if hasattr(self, "_sa_instance_state"):
            del cp_dct["_sa_instance_state"]
        return (cp_dct)
        # if getenv['STORAGE_TYPE'] == 'db':
        #     cp_dct.pop("password", None)

    def delete(self):
        """ Deletes an object from
        """
        models.storage.delete(self)