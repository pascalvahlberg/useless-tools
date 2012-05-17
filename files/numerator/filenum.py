#!/usr/bin/env python

from sys import argv, exit
from os import listdir, renames
from os.path import isdir, isfile

try:
	if len(argv) > 1 and len(argv) < 5:
		ext = "." + argv[1].lower()
		if argv[1].lower() == "-d":
			ext = ""
		elif argv[1].lower() == "-e":
			ext = "."

		prefix = ""
		suffix = ""
		if len(argv) > 2:
			prefix = argv[2] + "_"
			if len(argv) == 4:
				suffix = "_" + argv[3]

		c = 0
		
		files = listdir(".")
		files.sort()
		for name in files:
			if ext == "":
				if isdir(name):
					c += 1
			elif ext == ".":
				if isfile(name):
					if name[-5:].find(".") == -1:
						c += 1 
			elif name[-len(ext):].lower() == ext:
				c += 1

		for name in files:
			if ext == "":
				if isdir(name):
					print("% Temporary renaming '" + name + "/' to '" + name + "_tmp/'")
					renames(name, name + "_tmp")
			elif ext == ".":
				if isfile(name):
					if name[-5:].find(".") == -1:
						print("% Temporary renaming '" + name + "' to '" + name + "_tmp'")
						renames(name, name + "_tmp")
			elif name[-len(ext):].lower() == ext:
				print("% Temporary renaming '" + name + "' to '" + name[:-len(ext)] + "_tmp" + ext + "'")
				renames(name, name[:-len(ext)] + "_tmp" + ext)

		i = 1
		files = listdir(".")
		files.sort()
		for name in files:
			if ext == "":
				if isdir(name):
					newname = "0" * int(len(str(c)) - len(str(i))) + str(i)
					print("% Renaming '" + name + "/' to '" + prefix + newname + suffix + "/'")
					renames(name, prefix + newname + suffix)
					i += 1
			elif ext == ".":
				if isfile(name):
					if name[-5:].find(".") == -1:
						newname = "0" * int(len(str(c)) - len(str(i))) + str(i)
						print("% Renaming '" + name + "' to '" + prefix + newname + suffix + "'")
						renames(name, prefix + newname + suffix)
						i += 1
			elif name[-len(ext):].lower() == ext:
				newname = "0" * int(len(str(c)) - len(str(i))) + str(i) + ext
				print("% Renaming '" + name + "' to '" + prefix + newname + suffix + "'")
				renames(name, prefix + newname + suffix)
				i += 1

	else:
		print("FILENUM <extension> [prefix] [suffix]")
		print("  Special Extensions:")
		print("    -d Directories")
		print("    -e Extensionless files")

except Exception,e:
	print(e)
	exit(0)
except KeyboardInterrupt:
	print("CTRL + C")
	exit(0)

exit(0)