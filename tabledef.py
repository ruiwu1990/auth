# from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///auth.db', echo=True)
Base = declarative_base()

class User(Base):
	'''
	User class
	'''
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)

	def __init__(self, username, password):
		'''
		initialize function
		'''
		self.username = username
		self.password = password

Base.metadata.create_all(engine)