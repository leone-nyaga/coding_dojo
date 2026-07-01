#!/usr/bin/python3

import json


class Base:
    """
    Base class for managing object IDs.

    If an ID is provided during instantiation, it is used directly.
    Otherwise, an auto-incremented ID is assigned.

    Attributes:
        __nb_objects (int): Class-level counter tracking the
        number of objects created.
        id (int): Unique identifier for each instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

         Args:
            id: The ID to assign to the instance.
            If None, a unique ID is automatically generated.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)
