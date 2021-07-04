#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s):
   if s[i] == "W" and s[i + 4] == "y":
      print i
   i = i + 1
