from flask import render_template,request,redirect,url_for,abort
from . import main
from models import User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Welcome to Pitch Perfect'
   
    return render_template('index.html',title=title)

@main.route('/pitches')
def pitches():

    '''
    View pitches page function that returns the pitches details page and its data
    '''
    return render_template('pitches.html')

@main.route('/profile')
def profile():

    '''
    View profile page function that returns the profile details page and its data
    '''
    return render_template('profile.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

