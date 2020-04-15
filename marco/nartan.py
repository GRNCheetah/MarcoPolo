import functools
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('nartan', __name__)


STATIC_DIR = os.getcwd()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/download_page')
def download_page():

    # Find OS from User-Agent
    usrA = request.user_agent.string
  
    # Build implant depending on OS
    if usrA.find("Windows 10.0 NT 10.0"):
        name = 'windows 10'
    else:
        name = "Unknown OS"

    return render_template('download_page.html', name=name)

@bp.route('/download')
def download():
    return send_from_directory(STATIC_DIR, "test.py", as_attachment=True)

@bp.route('/aboutus')
def about_us():
    return render_template('about_us.html')