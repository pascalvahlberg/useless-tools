#!/usr/bin/env python

from sys import argv, exit
from os import listdir, renames, access, chdir, F_OK
from os.path import isdir, isfile

try:
	def red(string):
		return("\033[91m" + string + "\033[0m")

	def blue(string):
		return("\033[94m" + string + "\033[0m")

	def green(string):
		return("\033[92m" + string + "\033[0m")

	if len(argv) > 2 and len(argv) < 6:
		if argv[1].find(".") != -1:
			ext = argv[1].split(".")[-1].lower()
		else:
			ext = "." + argv[1].lower()

		if argv[1].lower() == "-d":
			ext = ""
		elif argv[1].lower() == "-e":
			ext = "."

		if access(argv[2], F_OK):
			if isdir(argv[2]):
				chdir(argv[2])
			else:
				exit(0)
		else:
			exit(0)

		prefix = ""
		suffix = ""
		if len(argv) > 3:
			prefix = argv[3]
			if len(argv) == 5:
				suffix = argv[4]

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
				if isfile(name):
					c += 1

		for name in files:
			if ext == "":
				if isdir(name):
					print(blue("*") + " Temporary renaming '" + name + "/' to '" + name + "_tmp/'")
					renames(name, name + "_tmp")
			elif ext == ".":
				if isfile(name):
					if name[-5:].find(".") == -1:
						print(blue("*") + " Temporary renaming '" + name + "' to '" + name + "_tmp'")
						renames(name, name + "_tmp")
			elif name[-len(ext):].lower() == ext:
				if isfile(name):
					print(blue("*") + " Temporary renaming '" + name + "' to '" + name[:-len(ext)] + "_tmp" + ext + "'")
					renames(name, name[:-len(ext)] + "_tmp" + ext)

		i = 1
		files = listdir(".")
		files.sort()
		for name in files:
			if ext == "":
				if isdir(name):
					newname = "0" * int(len(str(c)) - len(str(i))) + str(i)
					print(green("*") + " Renaming '" + name + "/' to '" + prefix + newname + suffix + "/'")
					renames(name, prefix + newname + suffix)
					i += 1
			elif ext == ".":
				if isfile(name):
					if name[-5:].find(".") == -1:
						newname = "0" * int(len(str(c)) - len(str(i))) + str(i)
						print(green("*") + " Renaming '" + name + "' to '" + prefix + newname + suffix + "'")
						renames(name, prefix + newname + suffix)
						i += 1
			elif name[-len(ext):].lower() == ext:
				if isfile(name):
					newname = "0" * int(len(str(c)) - len(str(i))) + str(i) + ext
					print(green("*") + " Renaming '" + name + "' to '" + prefix + newname + suffix + "'")
					renames(name, prefix + newname + suffix)
					i += 1

	else:
		print("FILENUM [<filename>.]<extension> <directory> [prefix] [suffix]")
		print("  Special Extensions:")
		print("    -d Directories")
		print("    -e Extensionless files")

except Exception,e:
	print(red("*") + " " + str(e))
	exit(0)
except KeyboardInterrupt:
	print("")
	print(red("*") + " CTRL + C")
	exit(0)

exit(0)