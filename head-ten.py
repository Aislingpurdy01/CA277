#!/usr/bin/env python

import sys

s = sys.stdin.readlines()

i = 0
while i < len(s) and i < 10:
   print s[i].strip()
   i = i + 1
