# -*- coding: utf8 -*-

from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper

class Codec(List):
    __mapper_args__ = {
        'polymorphic_identity':'codec'
    }
