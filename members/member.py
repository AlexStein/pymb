# -*- coding: utf8 -*-

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date
from base.database import Base

albums_members_table = Table('members_albums', Base.metadata,
    Column('album_id', Integer, ForeignKey('albums.id')),
    Column('member_id', Integer, ForeignKey('members.id'))
)

class Member(Base):
    __tablename__ = "members"
  
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    nickname = Column(String(255))
    instruments = Column(String(255))
    birthdate = Column(Date)
    gender = Column(String(16))
    country = Column(String(255))  