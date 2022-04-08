#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        import models
        from models.city import City

        city_dict = models.storage.all(City)
        temp = []
        for c_id in city_dict:
            if city_dict[c_id].state_id == self.id:
                temp.append(city_dict[c_id])
        return temp
