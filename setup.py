import os
import sys
import time
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
os.system('clear')
os.system('figlet -f small INSTALLING | lolcat')
print(yellow+'\n\t[+] X0N4Y3M SYSTEM INSTALLING...')
os.system('cd $HOME && cd X0N4Y3M && chmod +x *')
time.sleep(5)
os.system('cd $HOME && mv X0N4Y3M $PREFIX/bin && cd $PREFIX/bin/X0N4Y3M && mv toxic unistall-toxic $PREFIX/bin')
time.sleep(3)
print(green+'\n\t[+] ALMOST DONE! WAIT 3 SECOUND!')