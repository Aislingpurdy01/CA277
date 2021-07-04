#!/usr/bin/env python

import sys

header = sys.stdin.readline()
x = header.split(",")
field = sys.argv[1]
cities = sys.stdin.readlines()

i = 0
while i < len(cities):
   a = cities[i].strip().split(",")
   if a[9] == field:
      latitude = a[0] + "o" + a[1] + "'" + a[2] + '" ' + a[3] + ", "
      longitude = a[4] + "o" + a[5] + "'" + a[6] + '" ' + a[7]
      print a[8] + ":" + " " + latitude + longitude
   i = i + 1
