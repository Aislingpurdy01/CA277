#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
x = int(sys.argv[1])  # first line

i = 0
while i < len(s) and i < x:
   print s[i].strip()
   i = i + 1
