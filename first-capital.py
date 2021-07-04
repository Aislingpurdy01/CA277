#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s):
   if s[i] >= "A" and s[i] <= "Z":
      print str(s[i]) + " " + str(i)
      i = i + len(s)
   i = i + 1
