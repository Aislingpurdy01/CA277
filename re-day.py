#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
day = sys.argv[1]

i = 0
while i < len(lines):
   tokens = lines[i].split(",")
   day = tokens[8].split()
   if day[0] == sys.argv[1]:
      print lines[i].strip()
   i = i + 1
