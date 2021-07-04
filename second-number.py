#!/usr/bin/env python

s = raw_input()

t = 0
x = 0  # outter loop variable

while x < 2:
   i = t
   while i < len(s) and not (s[i] >= "0" and s[i] <= "9"):
      i = i + 1

   t = i
   while t < len(s) and (s[t] >= "0" and s[t] <= "9"):
      t = t + 1

   x = x + 1

if i < len(s):
   print s[i:t], i
