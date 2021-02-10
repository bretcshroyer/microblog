#load all sub-apps here
import subprocess

def app1():
    subprocess.call('launch.sh')

def app2():
    # pipe ps > log.txt
    #put log.txt into memory
    return('var')