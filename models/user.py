#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines the Class User """


class User(BaseModel):
    """ User that inherits from BaseModel

    Attributes:
        email (str): Public class Attribute for user email
        password (str): Public class Attribute for user password
        first_name (str): Public class Attribute for user first name
        last_name (str): Public class Attribute for user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Init method for User class

        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
