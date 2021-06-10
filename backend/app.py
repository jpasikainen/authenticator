from flask import Flask, request
from os import getenv
from db import db_session

app = Flask(__name__)
app.config["FLASK_ENV"] = getenv("FLASK_ENV")
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import routes