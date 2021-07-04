#!/usr/bin/env python

import sys

header = sys.stdin.readline()
cities = sys.stdin.readlines()

i = 0
while i < len(cities):
   a = cities[i].split(",")
   longitude = (int(a[4]) * 3600) + (int(a[5]) * 60) + int(a[6])
   if longitude > int(sys.argv[1]) and longitude < int(sys.argv[2]):
      print a[8] + ", " + a[9].strip()
   i = i + 1
