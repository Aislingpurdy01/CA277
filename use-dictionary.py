#!/usr/bin/env python

import dictionary

a = ["duck", "goose"]

i = 0

while i < len(a):
   s = a[i]
   if dictionary.has(s):
      print s + ":", dictionary.get(s) + "."
   i = i + 1

dictionary.set("lion", "Big cat")
