# -*- coding: utf8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base.database import Base

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    country = Column(String(255))

    # Связь с альбомами
    albums = relationship("Album", order_by="Album.id", backref="bands")
    
    def __init__(self, name=None, country=None):
        self.name = name
        self.country = country
        
    def __repr__(self):
        return '<Band %r>' % (self.name)        
