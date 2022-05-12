# from flask import redirect, render_template,url_for, request,flash
# from models import User
# from . import auth
# from werkzeug.security import generate_password_hash,check_password_hash
# from .forms import RegistrationForm
# from . import db
# from flask_login import login_user, login_required, logout_user, current_user
# from ..email import mail_message


# @auth.route('/sign-up')
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already exists.', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(first_name) < 2:
#             flash('First name must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(email=email, first_name=first_name, password=generate_password_hash(
#                 password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account created!', category='success')
#             return redirect(url_for('views.home'))

#     return render_template("sign_up.html", user=current_user)

# @auth.route('/login')
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 flash('Logged in successfully!', category='success')
#                 login_user(user, remember=True)
#                 return redirect(url_for('views.home'))
#             else:
#                 flash('Incorrect password, try again.', category='error')
#         else:
#             flash('Email does not exist.', category='error')

#     return render_template("login.html", user=current_user)


# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("main.index"))

# @auth.route('/signup', methods = ["GET","POST"])
# def signup():
#     form = RegForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data, password = form.password.data)
#         user.save_u()
#         mail_message("Welcome to Pitch-World","email/welcome_user",user.email,user=user)
#         return redirect(url_for('auth.login'))
#     return render_template('auth/signup.html', r_form = form)

from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import RegForm,LoginForm
from models import User
from .. import db
from ..email import mail_message

@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('auth/login.html', loginform = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        mail_message("Welcome to Pitch-Perfect","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', r_form = form)