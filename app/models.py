from app import db
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import hybrid
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property, relationship
from sqlalchemy import func
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Date,
    Boolean,
    Enum)

class CommonColumns(db.Model):
    __abstract__ = True
    _created = db.Column(DateTime, default=func.now())
    _updated = db.Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(40))

    @hybrid_property
    def _id(self):
        """
        Eve backward compatibility
        """
        return self.id

    def jsonify(self):
        """
        Used to dump related objects to json
        """
        relationships = inspect(self.__class__).relationships.keys()
        mapper = inspect(self)
        attrs = [a.key for a in mapper.attrs if \
                a.key not in relationships \
                and not a.key in mapper.expired_attributes]
        attrs += [a.__name__ for a in inspect(self.__class__).all_orm_descriptors if a.extension_type is hybrid.HYBRID_PROPERTY]
        return dict([(c, getattr(self, c, None)) for c in attrs])

#class User(CommonColumns):
#    id = db.Column(Integer, primary_key=True, autoincrement=True)
#    nickname = db.Column(db.String(64), index=True, unique=True)
#    email = db.Column(db.String(120), index=True, unique=True)
#
#    def __repr__(self):
#        return '<User %r>' % (self.nickname)

class Body(db.Model):
    __tablename__ = 'body'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True, unique=True)
    abrv = db.Column(db.String(64), index=True, unique=False)
    url  = db.Column(db.String(64), index=True, unique=False)

# class Clearances(CommonColumns):
#     __tablename__ = 'clearances'
#     id = db.Column(Integer, primary_key=True, autoincrement=True)
#     body_id = db.Column(Integer, ForeignKey('body.id',use_alter=True,name="body_fk"))
#     body = relationship(Body, uselist=False,post_update=True)
#     test = db.Column(String)
#     info = db.Column(String)
#
# class DogClearance(CommonColumns):
#     __tablename__ = 'dog_clearances'
#     dog_id = db.Column(Integer, ForeignKey('dogs.id',use_alter=True,name="dogs_fk"),primary_key=True)
#     clearance_id = db.Column(Integer, ForeignKey('clearances.id',use_alter=True,name="clearance_fk"),primary_key=True)
#
# class DogTitles(CommonColumns):
#     __tablename__ = 'dog_titles'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     dog_id = Column(Integer, ForeignKey('dogs.id',use_alter=True,name="dogs_fk"),primary_key=True)
#     title_id = Column(Integer, ForeignKey('titles.id',use_alter=True,name="titles_fk"),primary_key=True)

# class Dogs(CommonColumns):
#     __tablename__ = 'dogs'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     altered = Column(Boolean)
#     clearances = relationship("Clearances", secondary="dog_clearances", backref="dogs")
#     dam_id = Column(Integer, ForeignKey('dogs.id',use_alter=True,name="dams_fk"))
#     date_of_birth = Column(Date)
#     desc = Column(String)
#     registered_name = Column(String)
#     registrations = relationship("Registrations", secondary="dog_registrations", backref="dogs")
#     sex = Column('sexes',Enum("male", "female",name="sexes"))
#     sire_id = Column(Integer, ForeignKey('dogs.id',use_alter=True,name="sire_fk"))
#     titles = relationship("Titles", secondary="dog_titles", backref="dogs")
#     thumbnail = Column(String)
#     dam = relationship('Dogs', primaryjoin = ('Dogs.dam_id == Dogs.id'),lazy="joined",post_update=True)
#     sire = relationship('Dogs', primaryjoin = ('Dogs.sire_id == Dogs.id'),lazy="joined",post_update=True)
