#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0
day = input()

while i < len(a):
   line = a[i]
   x = line.split()
   if x[0] == str(day):
      print line
   i = i + 1
