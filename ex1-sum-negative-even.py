#!/usr/bin/env python

s = raw_input()
x = 0   # sum even and negative
y = 0   # sum of rest

while s != "end":
   if int(s) < 0 and int(s) % 2 == 0:
      x = x + int(s)
      s = raw_input()
   else:
      y = y + int(s)
      s = raw_input()

print x, y
