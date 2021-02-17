from flask import Flask, Blueprint, render_template, redirect, url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user,current_user 

from app import db, login_manager
from app.mod_auth.models import User
from app.mod_auth.forms import RegisterForm, LoginForm



mod_auth = Blueprint('auth', __name__)


@mod_auth.route('/register', methods=["POST","GET"])
def register():
    
    form = RegisterForm()

    if form.validate_on_submit():


        if User.query.filter_by(email=form.email.data).first():

            flash("You've already signed up with that email, log in instead!")

            return redirect(url_for('auth.login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = hash_and_salted_password
        )

        db.session.add(new_user)
        db.session.commit()

        #Important that this is after

        login_user(new_user)

    
        return redirect(url_for('home.get_all_posts'))



    return render_template("auth/register.html",form=form)



@mod_auth.route('/login/', methods=["GET","POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data


        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist") 
            return redirect(url_for('auth.login'))

        elif not check_password_hash(user.password, password):
            flash("That password is incorrect") 
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            return redirect(url_for('home.get_all_posts'))

    return render_template("auth/login.html", form=form)

@mod_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.get_all_posts'))