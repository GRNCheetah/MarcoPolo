# Marco and Polo
## A C2 and Implant Project for CS 4001

Marco is a website designed to look like a PC Speed-Up Tool to get your computer running as fast as it was on day one. It actually deploys Polo, which is the implant. Hopefully victims will visit the website and follow the download instructions to get the implant installed and running.

## Marco

#### To start Marco:  
This is a test version for right now, which only runs locally. Needs to be setup to run on a remote.  
Set an environment variable:  
  
Linux  
`FLASK_APP=marco`  
  
Windows Command Line  
`set FLASK_APP=marco`
    
Windows Powershell  
`$env:FLASK_APP = "marco"`  

Then run this in the project directory:   
`run flask`
  
Marco is a Flask application made with Flask. It has two functions:
1. Implanter
2. C2 Server

#### Implanter
Marco will serve the implant (Polo), posing as a PC Speed-Up Tool. Marco will then instruct the user on how to start the tool, effectively infecting their machine and allowing us full access to their machine. Marco will develop and deploy a Polo specific to the victim's machine. By reading the User-Agent, it makes a decision what instructions are needed.

#### C2 Server
Polo will have instructions to listen for instructions from Marco. Polo will be able to update it's toolbelt with updates from Marco. It will also be listening for tasks or arbitrary code to run and return info to Marco.

## Polo
#### Overall


#### Directory Structure
 * `cmds.txt`: Commands that need to be distributed to all infected clients are input here, after being ran the file will be cleared automatically via Marco.
 * `infected/`
    * Infected Host files will automatically be created here when an victim connects, all info regarding that specific implant is stored here.
 * `src`
    * Source code for building the implant, will be compiled by Marco upon victim connection.
