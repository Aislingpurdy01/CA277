#!/usr/bin/env python

import sys

header = sys.stdin.readline()
x = header.split(",")
field = sys.argv[1]
cities = sys.stdin.readlines()

i = 0
while i < len(cities):
   tokens = cities[i].strip().split(",")
   if tokens[9] == field:
      print tokens[8]  # print only city name
   i = i + 1
