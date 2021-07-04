#!/usr/bin/env python

import sys

header = sys.stdin.readline()  # read exactly 1 line from stdin
x = header.split(",")  # remove "," character
field = sys.argv[1].split("=")
position = 0

i = 0
while i < len(x):
   if x[i].strip() == field[0]:
      position = i
   i = i + 1

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   tokens = lines[i].strip().split(",")
   if field[1] == tokens[position].strip():
      print lines[i].strip()
   i = i + 1
