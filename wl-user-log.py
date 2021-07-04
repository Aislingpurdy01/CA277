#!/usr/bin/env python

a = []
user = raw_input()
s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0

while i < len(a):
   x = a[i].split()
   if x[1] == user:
      print " ".join(x)
   i = i + 1
