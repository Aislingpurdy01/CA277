#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0

while i < len(a):
   x = a[i].split()
   start = int(x[1])
   during = int(x[2])
   end = start + during - 1
   start = str(start) + ":00"
   end = str(end) + ":50"
   print x[0], start, end, " ".join(x[3:])
   i = i + 1
