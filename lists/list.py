# -*- coding: utf8 -*-

from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from base.database import Base

class List(Base):
    __tablename__ = 'lists'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    type = Column(String(32))

    __mapper_args__ = {
        'polymorphic_on':type,
    }
