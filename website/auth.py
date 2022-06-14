from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Notification
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


# User
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                # Notification
                new_notification = Notification(
                    message="New Login!", status="success", user_id=current_user.id)
                db.session.add(new_notification)
                db.session.commit()
                if user.accountType == "admin":
                    return redirect(url_for('views.adminDashboard', user=current_user))

                return redirect(url_for('views.home', user=current_user))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. Please Sign Up first.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        name = User.query.filter_by(first_name=first_name).first()

        if user:
            flash('Email already exists.', category='error')
        elif name:
            flash('Username already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 3:
            flash('First name must be greater than 2 characters.', category='error')
        elif len(first_name) > 8:
            flash('First name must be less than 9 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'), accountType="user")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            # Notification
            new_notification = Notification(
                message=f"Account Created. Welcome {first_name}!", status="success", user_id=current_user.id)
            db.session.add(new_notification)
            db.session.commit()
            return redirect(url_for('views.ticket'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/admin-signup', methods=['GET', 'POST'])
def admin_signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        secretcode = request.form.get('secretcode')

        user = User.query.filter_by(email=email).first()
        name = User.query.filter_by(first_name=first_name).first()

        if secretcode != "1234":
            flash('Incorrect Secret Code!', category='error')
        elif user:
            flash('Email already exists.', category='error')
        elif name:
            flash('Username already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 3:
            flash('First name must be greater than 2 characters.', category='error')
        elif len(first_name) > 8:
            flash('First name must be less than 9 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'), accountType="admin")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created as Admin!', category='success')
            # Notification
            new_notification = Notification(
                message=f"Admin Account Created. Welcome Admin {first_name}!", status="success", user_id=current_user.id)
            db.session.add(new_notification)
            db.session.commit()
            return redirect(url_for('views.adminDashboard', user=current_user))

    return render_template("admin_signup.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    # Notification
    new_notification = Notification(
        message="Logged Out!", status="error", user_id=current_user.id)
    db.session.add(new_notification)
    db.session.commit()

    logout_user()
    flash('Logged Out!', category='success')
    return redirect(url_for('auth.login'))
