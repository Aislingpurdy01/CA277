#!/usr/bin/env python

s = raw_input()

while s != "end":
   line = s.split(":")
   if line[6] != "/bin/false" and line[6] != "/usr/sbin/nologin":
      print line[0], line[6]
   s = raw_input()
