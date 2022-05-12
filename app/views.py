from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Welcome to Pitch Perfect'
   
    return render_template('index.html',title=title)

@app.route('/pitches')
def pitches():

    '''
    View pitches page function that returns the pitches details page and its data
    '''
    return render_template('pitches.html')

@app.route('/profile')
def profile():

    '''
    View profile page function that returns the profile details page and its data
    '''
    return render_template('profile.html')

@app.route('/sign-up')
def sign_up():

    '''
    View sign-up page function that returns the sign-up details page and its data
    '''
    return render_template('sign-up.html')

@app.route('/login')
def login():

    '''
    View login page function that returns the login details page and its data
    '''
    return render_template('login.html')

