#!/usr/bin/env python

s = raw_input()

while s != "end":
   line = s.split(":")
   s = raw_input()
   print line[0], line[6]
