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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    @property
    def cities(self):
        import models
        from models.city import City

        city_list = models.storage.all(City)
        temp = []
        for c_id in city_list:
            if city_list[c_id].state_id == self.id:
                temp.append(city_list[c_id])
        return temp
