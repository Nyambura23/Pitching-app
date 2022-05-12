from flask import render_template
from . import main

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

