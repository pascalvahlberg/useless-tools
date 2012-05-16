#!/usr/bin/env python

from sys import argv, exit
from os import listdir, rename

try:
	if len(argv) == 2:
		ext = "." + argv[1].lower()
		c = 0
		for name in listdir("."):
			if name[-4:].lower() == ext:
				c += 1

		for name in listdir("."):
			if name[-4:].lower() == ext:
				print("% Temporary renaming '" + name + "' to '" + name[:-4] + "_tmp" + ext)
				rename(name, name[:-4] + "_tmp" + ext)

		i = 1
		for name in listdir("."):
			if name[-4:].lower() == ext:
				newname = "0" * int(len(str(c)) - len(str(i))) + str(i) + ext
				print("% Renaming '" + name + "' to '" + newname + "'")
				rename(name, newname)
				i += 1

		print("% Renaming complete!")
	else:
		print("IMGNUM <extension>")

except Exception,e:
	print(e)
	exit(0)
except KeyboardInterrupt:
	print("CTRL + C")
	exit(0)

exit(0)