from flask import Flask, Blueprint, render_template, redirect, url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

from app import db
from app.mod_home.forms import CommentForm, CreatePostForm
from app.mod_home.models import BlogPost, Comment


mod_home = Blueprint('home', __name__)


@mod_home.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    print(current_user.is_authenticated)
    return render_template("home/index.html", all_posts=posts)

@mod_home.route("/post/<int:post_id>", methods=["GET","POST"])
def show_post(post_id):

    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    comments = Comment.query.filter_by(post_id = requested_post.id).all()



    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register")
            return redirect(url_for("auth.login"))

        new_comment = Comment(
            text = form.comment.data,
            author_id = current_user.id, 
            post_id = requested_post.id
        )
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('home.show_post',post_id=post_id))
   
    return render_template("home/post.html", post=requested_post, comments = comments, form=form, current_user = current_user)


@mod_home.route("/about")
def about():
    return render_template("home/about.html")


@mod_home.route("/contact")
def contact():
    return render_template("home/contact.html")