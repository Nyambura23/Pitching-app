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