import pyotp
from flask import request, session
from app import app
from models import User
from db import db_session
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

@app.route("/login", methods=["POST"])
def login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]

    if username and password:
        user = User.query.filter(User.username == username).first()
        if user and check_password_hash(user.password, password):
            session["username"] = username
            return {"status": "success", "redirect": "/authenticate"}
    return {"status": "failure"}

@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = session.get("username")
    if username:
        auth = Fernet(app.secret_key).decrypt(User.query.filter(User.username == username).first().auth)
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
            uri = pyotp.totp.TOTP(auth).provisioning_uri(name=email, issuer_name='Test App')
            f_auth = Fernet(app.secret_key).encrypt(bytes(auth, "utf-8"))
            h_password = generate_password_hash(password)
            user = User(username, email, h_password, f_auth)
            db_session.add(user)
            db_session.commit()

            return {"status": "success", "secret": uri}

    return {"status": "failure"}

@app.route("/user", methods=["GET"])
def user():
    return {"username": session.get("username", "")}