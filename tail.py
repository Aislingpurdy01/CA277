#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
x = int(sys.argv[1])

i = 0
while i < len(s) and i < x:
   if len(s) >= x:
      print s[len(s) - x + i].strip()
   else:
      print s[i].strip()
   i = i + 1
