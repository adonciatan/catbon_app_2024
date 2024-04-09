from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
# application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
# DBVAR=os.environ['DATABASE_URL']
# DBVAR="postgresql://username:os.environ.get(‘DB_PASSWORD’)@host:port/database"
# DBVAR="postgresql://username:password@host:port/database"
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
# application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

### Code computer
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'
DBVAR="postgresql://u750sgbrj4rvo3:p0afbd6fe1d96c0ce3d25d516cf759d9ba4d5c6c1e428988f7680969d40acdd1d@c2dr1dq7r4d57i.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d7betnh6r04sqj"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

