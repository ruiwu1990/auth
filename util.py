from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

def create_user(username, password):
	'''
	this function is used to insert new user into db
	'''
	engine = create_engine('sqlite:///auth.db', echo=True)
	# create session
	Session = sessionmaker(bind=engine)
	session = Session()

	user = User(username,password)
	session.add(user)

	session.commit()
	return

# create_user("rwu","admin")
# create_user("rwu1","admin")