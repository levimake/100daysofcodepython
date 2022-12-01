# Import Library platform and os
import platform
import os


def clrscr():
    # Check if the platform is Windows or linux
# If Platform is Windows then run command os.system(‘cls’) else os.system(‘clear’)
    if(platform.system().lower()=="windows"):
        cmdtorun='cls'
    else:
        cmdtorun='clear'

    os.system(cmdtorun)
