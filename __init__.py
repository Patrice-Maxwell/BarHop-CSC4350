from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from .auth import auth as auth_blueprint

db = SQLAlchemy()


def createapp():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://jfrudxnfhgiarz:37dbab76396127b98a5e05f2ce6ffa61dc24e9c9f7b9857273f0db644acff864@ec2-34-199-224-49.compute-1.amazonaws.com:5432/d5ciau5h4uuf4i"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.secret_key = b"os.getenv('APP_SECRET_KEY')"
    db.init_app(app)


app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint

app.register_blueprint(main_blueprint)

return app
