#launch on startup
#place in C:\Users\*USERNAME*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
#plays the classic Bonethugz song "First of the Month", so you can wake yo ass up and pay the rent.

import time
import webbrowser

url1 = "https://youtu.be/4j_cOsgRY7w"
url2 = "https://youtu.be/VMYAEHE2GrM"
testurl = "http://www.purple.com"

def special():
	if time.strftime("%d") == '01':
		if 9 < int(time.strftime("%H")) < 20:
			time.sleep(0.1)
			webbrowser.open(url1)
		else:
			exit()
	elif time.strftime("%d") == '15':
		if 9 < int(time.strftime("%H")) < 20:
			time.sleep(0.1)
			webbrowser.open(url2)
		else:
			exit()
	else:
		#webbrowser.open(testurl)
		exit()
	exit()

special()
