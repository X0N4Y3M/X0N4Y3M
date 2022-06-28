version='2.3.0'
import os
import sys
try:
    import requests
except:
    os.system('pip install requests')
import sys
import os
on_green="\033[42m"       # Green
blue="\033[0;34m"         # Blue
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
line=y+"==========================================================================="
logo=r+str("""\n\n\n    8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b\n\n\n""")
def header():
    print(logo+c+'\t\tDEVOLOPED BY : SABBIR AHMED\n\n'+g+'\t\t★★ FIND WEB SOURCE BY PYTHON ★★\n\n'+g+line)
while True:
    os.system('clear')
    header()
    w = requests.get(input(y+'\n\tENTER WEBSITE LINK : '+g))
    print(w.text)
    d = input('\n\ ')
    pass
    break