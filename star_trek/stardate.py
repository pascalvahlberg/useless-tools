#!/usr/bin/env python

from sys import exit
from time import time
from gtk import Clipboard

stardate_raw = str(time())
stardate = stardate_raw[1:6] + "," + stardate_raw[6]

print(stardate)

cb = Clipboard()
cb.set_text(stardate)
cb.store()

exit(0)