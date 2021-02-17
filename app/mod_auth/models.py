from app import db, login_manager, UserBase

from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(UserBase):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)

    posts = relationship("BlogPost", back_populates = "author")
    comments = relationship("Comment", back_populates = "comment_author")



    





