from flask import Flask
from flask_cors import CORS
from routes.site import blueprint
from routes.auth import auth_blueprint
import pymysql
from db import db

app = Flask(__name__)

CORS(app,origins=["http://localhost:8080"])
app.secret_key= 'juda_ishonchli_parol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://phpmyadmin:xroot@localhost/enigma'

db.init_app(app)
app.register_blueprint(blueprint,url_prefix='/')
app.register_blueprint(auth_blueprint,url_prefix='/auth')

if __name__ == '__main__':
	app.run()