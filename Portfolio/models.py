# To create table in postgres 

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import Relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    price = Column(Float, nullable = False)
    coins = Column(Float, nullable = False, server_default = '0.0')
    amount = Column(Float, nullable = False, server_default = '0.0')
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('NOW()'))
    # owner_id = Column(Integer, ForeignKey('Users.id', ondelete = 'CASCADE'), nullable = False)

    # owner = Relationship("User")