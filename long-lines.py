#!/usr/bin/env python

s = raw_input()
a = []

i = 0
while s != "end":
   a.append(s)
   s = raw_input()
   i = i + 1
n = input()

t = 0
while t < len(a):
   if len(a[t]) > n:
      print a[t]
   t = t + 1
