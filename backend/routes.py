import pyotp
from flask import request, session
from app import app
from models import User
from db import db_session

@app.route("/login", methods=["POST"])
def login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]

    if username and password:
        if User.query.filter(User.username == username).filter(User.password == password).first():
            session["username"] = username
            return {"status": "success", "redirect": "/authenticate"}
    return {"status": "failure"}

@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = session.get("username")
    if username:
        auth = User.query.filter(User.username == username).first().auth
        otp = request.get_json()["otp"]
        if pyotp.TOTP(auth).verify(otp):
            return {"status": "success"}
    return {"status": "failure"}
    

@app.route("/register", methods=["POST"])
def register():
    username = request.get_json()["username"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    
    if username and password and email:
        if not User.query.filter(User.username == username).first() and not User.query.filter(User.email == email).first():
            auth = pyotp.random_base32()
            secret = pyotp.totp.TOTP(auth).provisioning_uri(name=email, issuer_name='Test App')
            user = User(username, email, password, auth)
            db_session.add(user)
            db_session.commit()
            return {"status": "success", "secret": secret}

    return {"status": "failure"}