#!/usr/bin/env python

import sys

city = sys.argv[1]
lines = sys.stdin.readlines()[1:]

i = 0
while i < len(lines):
   tokens = lines[i].split(",")
   if tokens[1] == city:
      print lines[i].strip()
   i = i + 1
