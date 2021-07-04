#!/usr/bin/env python

s = raw_input()

x = 0

while s != "end":
   x = int(s) + x  # s to an integer
   s = raw_input()
print x
