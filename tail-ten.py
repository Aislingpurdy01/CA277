#!/usr/bin/env python

import sys

s = sys.stdin.readlines()

i = 0
while i < len(s) and i < 10:
   if len(s) >= 10:
      print s[len(s) - 10 + i].strip()
   else:
      print s[i].strip()
   i = i + 1
