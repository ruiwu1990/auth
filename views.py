'''
code is based on https://pythonspot.com/en/login-authentication-with-flask/
modified by Rui
'''

from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///auth.db', echo=True)

app = Flask(__name__)

@app.route("/")
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])
 
	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
	result = query.first()
	if result:
		session['logged_in'] = True
	else:
		flash('wrong password!')
	return index()


@app.route("/logout")
def logout():
	session['logged_in'] = False
	return index()

@app.route('/api/test_user/<test_username>/<test_password>')
def test_user(test_username='rwu',test_password='admin'):
	'''
	this function test if the user is in the db
	'''
	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([test_username]), User.password.in_([test_password]))
	result = query.first()
	if result:
		return "User in db"
	else:
		return "Cannot find user"

if __name__ == "__main__":
	app.debug = True
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=4000)