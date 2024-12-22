from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()

def create_app():
    app_name  = Flask(__name__)
    app_name.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'


    app_name.secret_key = 'SOME KEY'
 

    db.init_app(app_name)

    login_manager = LoginManager()
    login_manager.init_app(app_name)

    from models import User
    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app_name)

    #import later on
    from routes import register_routes

    register_routes(app_name, db, bcrypt)

    migrate = Migrate(app_name, db)


    return app_name

