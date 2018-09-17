from flask import render_template,url_for,flash
from . import main


# noinspection PyPackageRequirements
@main.route('/')
def index():

    '''
    View root function that returns the index page
    '''

    return render_template('index.html')