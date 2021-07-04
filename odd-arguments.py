#!/usr/bin/env python

import sys


i = 1
while i < len(sys.argv):
   if int(sys.argv[i]) % 2 != 0:
      print sys.argv[i]
   i = i + 1
