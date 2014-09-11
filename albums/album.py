# -*- coding: utf8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship, backref
from base.database import Base
from members.member import albums_members_table

class Album(Base):
    __tablename__ = 'albums'
    
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    name = Column(String(255))
    release_type = Column(String(255))
    disks_count = Column(Integer)
    year = Column(Integer)
    style = Column(String(255))
    codec = Column(String(255))
    bitrate = Column(Integer)
    vbr = Column(Boolean) 
    length = Column(Integer)
    tracks_count = Column(Integer)
    label = Column(String(255))
    release_date = Column(Date)
    update_date = Column(Date)
    
    # Ссылка на Группу
    band = relationship("Band", backref=backref('bands', order_by=id))

    members = relationship("Member", 
                           secondary=albums_members_table,
                           backref="albums")