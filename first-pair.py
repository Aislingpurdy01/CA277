#!/usr/bin/env python

s = raw_input()

i = 1
while i < len(s) and s[i] != s[i - 1]:
   position = i
   i = i + 1

if i < len(s):
   print s[i] + s[i - 1]
