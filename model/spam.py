# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from db import db,SQLAlchemy

class Spam(db.Model):
	'''  Spam model '''
	__tablename__ = 'spam'

	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	status = db.Column(db.String)
	message = db.Column(db.Text)
	date = db.Column(db.Date)

	def __repr__(self):
		return f'<Spam {self.status} >'