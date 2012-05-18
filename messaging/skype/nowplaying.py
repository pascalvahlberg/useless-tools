#!/usr/bin/env python

import Skype4Py
from urllib2 import urlopen
from time import sleep
from sys import exit

try:
	skype = Skype4Py.Skype()
	skype.Attach()
except Exception,e:
	print(e)
	exit(0)
except KeyboardInterrupt:
	print("")
	print("CTRL + C")
	exit(0)

print("Enter the path or the url to your song file:")
path = raw_input()
if path.startswith("http://"):
	print("Okay: It's an url!")
	song = ""
	while 1:
		try:
			getsong = urlopen(path).read().rstrip()
			if song != getsong:
				song = getsong
				skype.Profile("MOOD_TEXT", unicode(song) + " (Now-Playing from Chiruclan)")
			sleep(2)
		except Exception,e:
			print(e)
			pass
		except KeyboardInterrupt:
			print("")
			print("CTRL + C")
			exit(0)
else:
	print("Okay: It's a file!")
	song = ""
	while 1:
		try:
			getsong = file(path).read().rstrip()
			if song != getsong:
				song = getsong
				skype.Profile("MOOD_TEXT", unicode(song) + " (Now-Playing by Chiruclan)")
			sleep(2)
		except Exception,e:
			print(e)
			pass
		except KeyboardInterrupt:
			print("")
			print("CTRL + C")
			exit(0)

print("Exiting...")
	
exit(0)