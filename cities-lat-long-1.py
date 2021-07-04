#!/usr/bin/env python

import sys

header = sys.stdin.readline()
x = header.split(",")
field = sys.argv[1]
field2 = sys.argv[2]
cities = sys.stdin.readlines()

i = 0
while i < len(cities):
   a = cities[i].strip().split()
   if a[9] == field2 and a[8] == field:
      latitude = (int(a[0]) * 3600) + (int(a[1]) * 60) + int(a[2])  # turning to an interger
      longitude = (int(a[4]) * 3600) + (int(a[5]) * 60) + int(a[6])
      print str(latitude) + " " + str(longitude)  # print the string of each
   i = i + 1
