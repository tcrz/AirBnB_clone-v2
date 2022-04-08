#!/usr/bin/python3
"""
DBstorage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBstorage:
    """defines DBstorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """initialise instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """query on the current database session (self.__session) all
        objects depending of the class name"""
        all_obj = {}
        if cls is not None:
            for row in self.__session.query(cls):
                key = row.__class__.__name__ + '.' + row.id
                all_obj.update({key: row})
            return all_obj
        else:
            models = {mapper.class_.__name__: mapper.class_
                      for mapper in Base.registry.mappers}
            for key in list(models.keys()):
                for row in self.__session.query(models[key]):
                    key = row.__class__.__name__ + '.' + row.id
                    all_obj.update({key: row})
            return all_obj

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        "creates all tables in database and current database session"
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session
        attribute (self.__session)"""
        self.__session.close()
