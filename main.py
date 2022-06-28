version='2.3.0'
import os
import sys
import time
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
off=red+"\n\n\n\t\tYOU ARE BANNED FOR 4 HOURS PLEASE MEET THIS CREATOR OWNER\n\n"
delete=red+'\n\n\n\t\tYOUR DDOS-ATTACK SYSTEM IS UNISTALLING IN 5 SECOND\n\n'
line=yellow+"==========================================================================="+end
logo=red+str("""\n\n\n    8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b\n\n""")+end
def header():
    print(logo+cyan+'\n\t\tDEVOLOPED BY : SABBIR AHMED\n\n'+green+'\t\tVERSION : '+ str(version)+'\n\n'+end+line)
count=1
erase = '\x1b[1A\x1b[2K'
count=1
os.system('clear')
header()
print(cyan+'\n\t\t[•] CHECKING FOR UPDATES\n\t\t')
time.sleep(0.7)

while count<2:
	os.system('clear')
	header()
	print(yellow+"\n\t  [1] ONE CLICK RUN\n\n\t  [2] ENCRYPT/OBFUSCATE SCRIPT\n\n\t  [3] BD SMS BOMBER\n\n\t  [4] WEB INFO\n\n\t  [5] DDOS-ATTACK \n\n\t")
	main_opt=str(input(blue+"\n\t[>] SELECT YOUR OPTION : "+yellow))
	if main_opt=='1':
	    os.system('python setup.py')
	elif main_opt=='2':
	    os.system('python enc.py')
	elif main_opt=='3':
	    os.system('python3 S.py')
	elif main_opt=='4':
	    os.system('python3 W.py')
	elif main_opt=='5':
	    os.system('python2 ddos-attack.py')
	 
	else:
		os.system('clear')
		notice=red+"\t\t[×] Wrong Option Entered!"
		count=1
