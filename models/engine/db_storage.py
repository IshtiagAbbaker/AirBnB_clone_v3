#!/usr/bin/python3
""" Database engine """

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """handles long term storage of all class instances"""
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }

    """ handles storage for database """
    __engine = None
    __session = None

    def __init__(self):
        """ creates the engine self.__engine """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB')))
        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
<<<<<<< HEAD
        """query on the current database session"""
        nw_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    nw_dict[key] = obj
        return (nw_dict)

    def new(self, obaj):
        """add the object to the current database session"""
        self.__session.add(obaj)
=======
        """ returns a dictionary of all objects """
        obj_dict = {}
        if cls:
            obj_class = self.__session.query(self.CNC.get(cls)).all()
            for item in obj_class:
                key = str(item.__class__.__name__) + "." + str(item.id)
                obj_dict[key] = item
            return obj_dict
        for class_name in self.CNC:
            if class_name == 'BaseModel':
                continue
            obj_class = self.__session.query(
                self.CNC.get(class_name)).all()
            for item in obj_class:
                key = str(item.__class__.__name__) + "." + str(item.id)
                obj_dict[key] = item
        return obj_dict

    def new(self, obj):
        """ adds objects to current database session """
        self.__session.add(obj)
>>>>>>> 2796a9e7e0ec4944989c635eb139550a458166e0

    def get(self, cls, id):
        """
        fetches specific object
        :param cls: class of object as string
        :param id: id of object as string
        :return: found object or None
        """
        all_class = self.all(cls)

        for obj in all_class.values():
            if id == str(obj.id):
                return obj

        return None

    def count(self, cls=None):
        """
        count of how many instances of a class
        :param cls: class name
        :return: count of instances of a class
        """
        return len(self.all(cls))

    def save(self):
        """ commits all changes of current database session """
        self.__session.commit()

<<<<<<< HEAD
    def delete(self, obaj=None):
        """delete from the current database session obj if not None"""
        if obaj is not None:
            self.__session.delete(obaj)
=======
    def delete(self, obj=None):
        """ deletes obj from current database session if not None """
        if obj is not None:
            self.__session.delete(obj)
>>>>>>> 2796a9e7e0ec4944989c635eb139550a458166e0

    def reload(self):
        """ creates all tables in database & session from engine """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__session.remove()
<<<<<<< HEAD

    def get(self, clas, id):
        """Retrieve an object"""
        if clas is not None and type(clas) is str and id is not None and\
           type(id) is str and clas in name2class:
            clas = name2class[clas]
            result = self.__session.query(clas).filter(clas.id == id).first()
            return result
        else:
            return None

    def count(self, clas=None):
        """Count number of objects in storage"""
        total = 0
        if type(clas) == str and clas in name2class:
            clas = name2class[clas]
            total = self.__session.query(clas).count()
        elif clas is None:
            for clas in name2class.values():
                total += self.__session.query(clas).count()
        return total
=======
>>>>>>> 2796a9e7e0ec4944989c635eb139550a458166e0
