#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines the class City"""


class City(BaseModel):
    """Public Attributes for the class City

    Attribute:
        state_id: (Str) - empty string
        name: (str) - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init method for User class

        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
