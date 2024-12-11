from flask import Blueprint
from controller.sitecontroller import index,analiz,spam

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/',methods=['GET'])(index)
blueprint.route('/analiz',methods=['GET'])(analiz)
blueprint.route('/spam',methods=['GET'])(spam)