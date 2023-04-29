from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_seasurf import SeaSurf
from flask_talisman import Talisman

db = SQLAlchemy()

DB_NAME = "database.db"
SELF = "'self'"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    csrf = SeaSurf(app)
    csrf.init_app(app)

    # Token required in every form for security:
    # <input type="hidden" name="_csrf_token" value="{{csrf_token()}}">

    db.init_app(app)

    talisman = Talisman(
        app,
        content_security_policy={
            'default-src': SELF,
            'img-src': '*',
            'script-src': [
                SELF,
                'bootstrapcdn.com',
                'cloudflare.com',
                'jquery.com'
            ],
            'style-src': [
                SELF,
                'bootstrapcdn.com',
                'cloudflare.com',
                'jquery.com',
            ],
        },
        content_security_policy_nonce_in=['script-src'],
        feature_policy={
            'geolocation': '\'none\'',
        }
    )
    talisman.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
