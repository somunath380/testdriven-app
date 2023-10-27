# from project import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(128), nullable=False)
    email = mapped_column(String(128), nullable=False)
    active = mapped_column(Boolean, default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email