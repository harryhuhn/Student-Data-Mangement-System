from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    appl = Flask(__name__)
    appl.config['SECRET_KEY'] = 'hawk'
    appl.config['SWLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(appl)
    from .views import views
    from .auth import auth
    appl.register_blueprint(views, url_prefix='/')
    appl.register_blueprint(auth, url_prefix='/')
    from .models import User, Note
    create_database(appl)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(appl)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return appl

def create_database(appl):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=appl)
        print('Created Database')