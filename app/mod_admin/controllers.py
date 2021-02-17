from flask import Flask, Blueprint, render_template, redirect, url_for,flash, abort
from flask_login import current_user

from app import db
from app.mod_home.forms import CommentForm, CreatePostForm
from app.mod_home.models import BlogPost, Comment

from datetime import datetime


mod_admin = Blueprint('admin', __name__)

def admin_only(f):
    def wrapper_function(*args, **kwargs):
        if current_user.id !=1:
            return abort(403)
        return(f(*args, **kwargs))
    wrapper_function.__name__ = f.__name__
    return wrapper_function


@mod_admin.route("/new-post", methods=["GET","POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=datetime.now().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home.get_all_posts"))
    return render_template("admin/make-post.html", form=form)


@mod_admin.route("/edit-post/<int:post_id>", methods = ["POST","GET"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("home.show_post", post_id=post.id))

    return render_template("admin/make-post.html", form=edit_form)


@mod_admin.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home.get_all_posts'))

