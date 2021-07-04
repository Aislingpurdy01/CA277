#!/usr/bin/env python

a = []

s = raw_input()

while s != "end":
   a.append(s)
   s = raw_input()

i = 0
total = 0

while i < len(a):
   x = a[i].split("/")
   if x[len(x) - 1] == "upload":
      total = total + 1
   i = i + 1
print total
