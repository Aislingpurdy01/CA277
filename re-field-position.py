#!/usr/bin/env python

import sys

header = sys.stdin.readline()  # read exactly 1 line for stdin and return it
x = header.split(",")  # split "," character
field = sys.argv[1]  # first command-line argument

i = 0
while i < len(x):
   if x[i].strip() == field:
      print i
   i = i + 1
