from app import db, login_manager

from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(UserMixin,db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)


    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)


    posts = relationship("BlogPost", back_populates = "author")
    comments = relationship("Comment", back_populates = "comment_author")


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))



    





