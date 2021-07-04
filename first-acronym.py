#!/usr/bin/env python

s = raw_input()


i = 0

while i < len(s) and not (s[i] >= "A" and s[i] <= "Z"):
   i = i + 1

a = ""  # acronym
position = i
if i < len(s):
   while i < len(s) and s[i] >= "A" and s[i] <= "Z":
      a = a + s[i]
      i = i + 1
   print a + " " + str(position)
