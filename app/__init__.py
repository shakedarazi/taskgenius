from flask import Flask
from .routes import main
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'  # נחליף אותו במשתנה סביבה בהמשך

    
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

