from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper
from lists.list import List

class Codec(List):
    __mapper_args__ = {
        'polymorphic_identity':'codec'
    }

    def __init__(self, name=None):
        self.name = name
        self.codec = 'codec'