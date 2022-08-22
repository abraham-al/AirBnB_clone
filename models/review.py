#!/usr/bin/python3
"""Defines The Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """Public Class Atrributes
    Attributes
        place_id: (Str) - empty string: it will be the Place.id
        user_id: (Str) - empty string: it will be the User.id
        text: (Str) - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Init method for User class

        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
