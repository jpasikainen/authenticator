from sqlalchemy import Column, Integer, String, LargeBinary
from db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(500))
    auth = Column(LargeBinary())

    def __init__(self, username=None, email=None, password=None, auth=None):
        self.username = username
        self.email = email
        self.password = password
        self.auth = auth

    def __repr__(self):
        return f'<User {self.username!r}>'
