#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0

while i < len(a):
   x = a[i].split()
   if int(x[2]) > 7500:
      print a[i]
   i = i + 1
