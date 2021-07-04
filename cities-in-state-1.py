#!/usr/bin/env python

import sys

header = sys.stdin.readline()
x = header.split(",")
cities = sys.stdin.readlines()
field = sys.argv[1]

i = 0
while i < len(cities):
   tokens = cities[i].strip().split(",")
   if tokens[9] == field:
      print cities[i].strip()
   i = i + 1
