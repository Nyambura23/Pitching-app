from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Pitch Perfect'
    return render_template('index.html',message=message)

@app.route('/pitches')
def pitches():

    '''
    View pitches page function that returns the pitches details page and its data
    '''
    return render_template('pitches.html')

@app.route('/pitches')
def profile():

    '''
    View profile page function that returns the profile details page and its data
    '''
    return render_template('profile.html')