#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
   i = i + 1

if i < len(s):
   t = i
   while t < len(s) and "0" <= s[t] and s[t] <= "9":
      t = t + 1

   print s[i:t] + " " + str(i)
