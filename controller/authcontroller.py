from flask import jsonify,request
from model.user import User,db
import sqlalchemy
import sqlalchemy.orm
# from flask_bcrypt import check_password_hash

def login():
	login = request.args.get('login')
	password = request.args.get('password')

	user = User.query.filter_by(login=login).first()

	if not user:
		return jsonify({
			'status':'flase'
		})

	return jsonify({
		'login':user.login,
		'pass':user.password
	})


def user():
	return jsonify(True)