from db import db_session
from models import User
import pyotp

name = input("Username: ")
email = input("Email: ")
password = input("Password: ")
rb32 = pyotp.random_base32()

u = User(name, email, password, rb32)

db_session.add(u)
db_session.commit()