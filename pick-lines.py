#!/usr/bin/env python

import sys

s = sys.stdin.readlines()

i = 1  # start at 1 because first element is name of script
while i < len(sys.argv):
   print s[int(sys.argv[i])].strip()
   i = i + 1
