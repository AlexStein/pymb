# -*- coding: utf8 -*-

from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper

class Style(List):
    
    __mapper_args__ = {
        'polymorphic_identity':'style'
    }
