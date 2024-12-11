from db import db, SQLAlchemy

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	login = db.Column(db.String(255))
	password = db.Column(db.String(255))
	role = db.Column(db.String())

	def __init__(self, login, password, role = 'admin'):
		self.login = login
		self.password = password
		self.role = role

	def __repr__(self):
		return f'<User {self.login}>'