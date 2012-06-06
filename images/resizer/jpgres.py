#!/usr/bin/env python

from sys import argv, exit
from os import listdir
from fnmatch import fnmatch
from PIL import Image

try:
	def red(string):
		return("\033[91m" + string + "\033[0m")

	def blue(string):
		return("\033[94m" + string + "\033[0m")

	def green(string):
		return("\033[92m" + string + "\033[0m")

	if len(argv) == 3 or len(argv) == 4:
		for file in sorted(listdir(".")):
			if fnmatch(file.lower(), "*.jpg"):
				print(blue("*") + " Opening image '" + file + "'")
				img = Image.open(file)
				old_size = img.getprojection()
				y_axis_old = len(old_size[0])
				x_axis_old = len(old_size[1])
				if argv[1] == "+":
					y_axis = len(old_size[0]) * int(argv[2])
					x_axis = len(old_size[1]) * int(argv[2])
				elif argv[1] == "-":
					y_axis = len(old_size[0]) / int(argv[2])
					x_axis = len(old_size[1]) / int(argv[2])

				new_size = (y_axis, x_axis)
				print(blue("*") + " Resizing picture from '" + str(y_axis_old) + "x" + str(x_axis_old) + "' to '" + str(y_axis) + "x" + str(x_axis) + "'")
				img.thumbnail(new_size, Image.ANTIALIAS)
				if argv[3] == "-o":
					print(green("*") + " Saving image to '" + file + "'")
					img.save(file, "JPEG")
				else:
					print(green("*") + " Saving image to '" + file[:-4] + "_" + str(y_axis) + "x" + str(x_axis) + file[-4:] + "'")
					img.save(file[:-4] + "_" + str(y_axis) + "x" + str(x_axis) + file[-4:], "JPEG")
	else:
		print("JPGRES <+/-> <factor> [-o]")

except Exception,e:
	print(red("*") + " " + str(e))
	exit(0)
except KeyboardInterrupt:
	print("")
	print(red("*") + " CTRL + C")
	exit(0)

exit(0)