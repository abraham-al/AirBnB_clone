#!/usr/bin/python3

from models.base_model import BaseModel
"""Defines the Class Place"""


class Place(BaseModel):
    """Public class attributes for the class Place

        Attributes:

            city_id: (Str) - empty string: it will be the City.id
            user_id: (Str) - empty string: it will be the User.id
            name: (Str) - empty string
            description: (Str) - empty string
            number_rooms: (Int) - 0
            number_bathrooms: (Int) - 0
            max_guest: (Int) - 0
            price_by_night: (Int) - 0
            latitude: (float) - 0.0
            longitude: (float_ - 0.0
            amenity_ids: list: Str - empty list: it will be the
            list of Amenity.id later

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Init method for User class

        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
