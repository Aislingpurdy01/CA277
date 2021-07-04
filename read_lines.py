#!/usr/bin/env python

def get():
   s = raw_input()
   a = []

   while s != "end":
      a.append(s)
      s = raw_input()

   return a
