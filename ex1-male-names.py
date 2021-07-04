#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0

while i < len(a):
   name = a[i]
   x = name.split(",")
   if x[0] == "m":
      print name
   i = i + 1
