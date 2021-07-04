#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0
while i < len(a):
   tokens = a[i].split()
   print " ".join(tokens[5:])
   i = i + 1
