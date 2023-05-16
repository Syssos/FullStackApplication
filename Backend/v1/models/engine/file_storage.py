#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hocus Pocus File Storage

The class defined in this file will be used through out the application
to add, change, remove, or view data saved in a file. The file format
of choice is JSON. There is an array of objects stored in a file called
"file.json" containing all of the data used by this file. The database
equivalant of this class will use the same data, however access it via
database connection.

FileStoragedoes has 2 attributes initial assigned to it. You can
find more details on these attributes below. The initial decloration of 
the FileStorage class is held within the "__init__.py" file located in
"/models/__init__.py". For more information on each of the methods of 
this class please see the comment at the top of each method decloration.

__file_path - String, The file location on disk used to gather and store data
__objects - Dictionary/Object, Temporary location in memory of data pulled and pushed to file located at "__file_path"
"""

# Standard library imports
import json

# Local application/library specific imports
import models


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def reload(self):
        '''
            Return: None
            This function will load the data from __file_path into the __objects data,
            effectively pulling in any new changes on the data in the file. Useful after
            saving data to file, or initially loading data when the programs first started.
        '''

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def close(self):
        '''
            Here for future use, This function does not commit changes.

            Should commit any changes within __objects into file located 
            at __file_path and close fd, check to see if fd can be closed 
            later, simular to defer statement in Go?
        '''
        self.reload()

    def save(self):
        '''
            Here for future use, This function does not commit changes.

            Should commit any changes within __objects into file located 
            at __file_path.
        '''
        self.reload()

    def delete(self):
        '''
            Here for future use, This function does not commit changes.

            Should delete object, then commit changes within in file located 
            at __file_path.
        '''
        self.reload()

    def all(self, cls=None):
        '''
            Return ex 
            {
                "__class__.__name__.SKU": {atr: "data", atr: "data", ...}, 
                "Ram.AV9875KJG": {SKU: "AV9875KJG", Speed: 2666, ...},
                ...
            }

            Returns dictionary of all instances of the scpecified class found within __objects
        '''
        new_dict = {}
        if cls is None:
            return self.__objects

        if cls is not None and cls != "":
            for k, v in self.__objects.items():
                if cls == k.split(".")[0]:
                    new_dict[k] = v
            return new_dict
        else:
            return self.__objects

    def get(self, cls, sku_id):
        ''' 
            Returns an object with corresponding SKU_id number
        '''
        cls_dict = self.all(cls)
        val = "{}.{}".format(str(cls), str(sku_id))
        obj = cls_dict.get(val)
        return obj

    def count(self, cls=None):
        '''
            Returns the number of each instance found for "cls" in self.__object
        '''
        count = 0
        cls_dict = self.all(cls)
        count = len(cls_dict)
        return count