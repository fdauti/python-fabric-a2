from fabric.api import *
'''
OPS435 Assignment 2S - Win 2021
Program: a2s_fdauti.py
Author: Fatjon Dauti
The python code in this file a2s_fdauti.py is original work written by
Fatjon Dauti. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''
env.user = "student"
env.port = '7904'
env.hosts = ['myvmlab.senecacollege.ca']

def addUser(name):
    '''add a user with given user name to remote system'''
    cmd = "grep ^"+name+" /etc/passwd"
    result = run(cmd, warn_only=True, quiet=True)
    if result.failed:
        sudo("useradd -m "+name)
        print("User '"+name+"' added!")
    else:
        print("User '"+name+"' already exists!")

def findUser(name):
    '''find user with a given user name'''
    cmd = "grep ^"+name+" /etc/passwd"
    result = run(cmd, warn_only=True, quiet=True)
    if result.succeeded:
        print("Found user '"+name+"' on the system!")
    else:
        print("User '"+name+"' NOT found!")

def listUser():
    '''return a list of shell user on a remote system'''
    cmd = "grep /bin/bash$ /etc/passwd | cut -d: -f1"
    result = run(cmd)
    print(result.split())

def listSysUser():
    '''return a list of system (non-shell) user'''
    cmd = "grep -v /bin/bash$ /etc/passwd | cut -d: -f1"
    result = run(cmd)
    print(result.split())