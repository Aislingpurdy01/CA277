#!/usr/bin/env python

import sys

s = sys.stdin.readlines()
a = []

i = 0  # start at 0 because want to print out first number
while i < len(s):
   if int(s[i]) % 2 != 0:
      print s[i].strip()
   i = i + 1
