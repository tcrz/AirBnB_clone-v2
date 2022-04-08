#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref="place")
        amenities = relationship('Amenity', secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        from models import storage

        @property
        def reviews(self):
            from models.review import Review

            review_list = models.storage.all(Review)
            linked_reviews = []
            for obj_id in review_list:
                if review_list[obj_id].place_id == self.id:
                    linked_reviews.append(review_list[obj_id])
            return linked_reviews

        @property
        def amenities(self):
            """method to get amenity instances linked to this place"""
            from models.amenity import Amenity

            amn_dict = storage.all(Amenity)
            linked_amn = []
            for obj_id in amn_dict:
                if amn_dict[obj_id].id == self.id:
                    linked_amn.append(amn_dict[obj_id])
            return linked_amn

        @amenities.setter
        def append(self, amenity_obj):
            """method to add an amenity to list of amenities"""
            if amenity_obj.__class__.__name__ == "Amenity":
                amenity_ids.append(amenity_obj.id)
