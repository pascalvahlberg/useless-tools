#!/usr/bin/env python

import Skype4Py
from urllib2 import urlopen
from time import sleep
from sys import exit

try:
	skype = Skype4Py.Skype()
	skype.Attach()

	print("Enter the path or the url to your song file:")
	path = raw_input()
	if path.startswith("http://"):
		print("Okay: It's an url!")
		song = ""
		while 1:
			getsong = urlopen(path).read().rstrip()
			if song != getsong:
				song = getsong
				skype.Profile("MOOD_TEXT", song + " (Now-Playing from Chiruclan)")
			sleep(2)
	else:
		print("Okay: It's a file!")
		song = ""
		while 1:
			getsong = file(path).read().rstrip()
			if song != getsong:
				song = getsong
				skype.Profile("MOOD_TEXT", song + " (Now-Playing by Chiruclan)")
			sleep(2)

	print("Exiting...")

except Exception,e:
	print(e)
	exit(0)
except KeyboardInterrupt:
	print("")
	print("CTRL + C")
	exit(0)

exit(0)