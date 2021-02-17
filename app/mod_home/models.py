from app import db,login_manager

from sqlalchemy.orm import relationship
from app.mod_auth.models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)



class BlogPost(db.Model):

    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    #Foreign Key -> User
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates = "posts")

    comments = relationship("Comment", back_populates = "parent_post")



class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    #Foreign Key -> User

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")   


    #Foreign Key -> BlogPost

    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")