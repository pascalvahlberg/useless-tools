#!/usr/bin/env python

import Skype4Py
from urllib2 import urlopen
from time import sleep
from sys import argv, exit

if len(argv) == 2:
	path = argv[1]

	try:
		skype = Skype4Py.Skype()
		skype.Attach()
		oldmood = skype.Profile("MOOD_TEXT")
	except Exception,e:
		print(e)
		exit(0)
	except KeyboardInterrupt:
		print("")
		print("CTRL + C")
		exit(0)

	if path.startswith("http://"):
		print("Okay: It's an url!")
		song = ""
		while 1:
			try:
				getsong = urlopen(path).read().rstrip()
				if song != getsong:
					song = getsong
					skype.Profile("MOOD_TEXT", unicode(song.encode('utf-8')) + " (Now-Playing from Chiruclan)")
					print("Updated song: " + song)
				sleep(2)
			except Exception,e:
				print(e)
				pass
			except KeyboardInterrupt:
				print("")
				print("CTRL + C")
				skype.Profile("MOOD_TEXT", oldmood)
				exit(0)
	else:
		print("Okay: It's a file!")
		song = ""
		while 1:
			try:
				getsong = file(path).read().rstrip()
				if song != getsong:
					song = getsong
					skype.Profile("MOOD_TEXT", unicode(song.encode('utf-8')) + " (Now-Playing by Chiruclan)")
					print("Updated song: " + song)
				sleep(2)
			except Exception,e:
				print(e)
				pass
			except KeyboardInterrupt:
				print("")
				print("CTRL + C")
				skype.Profile("MOOD_TEXT", oldmood)
				exit(0)

	try:
		skype.Profile("MOOD_TEXT", oldmood)
	except Exception,e:
		print(e)
		exit(0)
	except KeyboardInterrupt:
		print("")
		print("CTRL + C")
		exit(0)
else:
	print("NOWPLAYING.PY <path/url>")
	
exit(0)