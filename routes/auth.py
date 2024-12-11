from flask import Blueprint
from controller.authcontroller import login, user

auth_blueprint = Blueprint('auth_blueprint', __name__)


auth_blueprint.route('/login',methods=['GET'])(login)
auth_blueprint.route('/profile',methods=['GET'])(user)