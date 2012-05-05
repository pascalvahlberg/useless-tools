#!/usr/bin/env python

from sys import exit
from time import time

stardate_raw = str(time())
stardate = stardate_raw[1:6] + "," + stardate_raw[6]

print(stardate)

exit(0)