#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0

while i < len(a):
   x = a[i].split()
   if 1 < int(x[2]):
      print " ".join(x)
   i = i + 1
