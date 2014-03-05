from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper
from lists.list import List

class Country(List):
    __mapper_args__ = {
        'polymorphic_identity':'country'
    }
