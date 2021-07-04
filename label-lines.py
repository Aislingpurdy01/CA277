#!/usr/bin/env python

s = raw_input()
a = []

i = 0
while s != "end":
   a.append(s)
   s = raw_input()
   i = i + 1

b = 0
while b < len(a):
   print b, len(a), a[b]
   b = b + 1
