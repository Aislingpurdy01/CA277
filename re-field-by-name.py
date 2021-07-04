#!/usr/bin/env python

import sys

header = sys.stdin.readline()  # read exactly 1 line from stin
x = header.split(",")  # split "," character from header
field = sys.argv[1]  # first command-line argument

i = 0
position = 0  # position of the field
while i < len(x):
   if x[i].strip() == field:
      position = i
   i = i + 1

lines = sys.stdin.readlines()  # comnsumes all of input

i = 0
while i < len(lines):
   tokens = lines[i].strip().split(",")
   print tokens[position]
   i = i + 1
