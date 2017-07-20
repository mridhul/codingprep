#!/bin/python

import sys
import string


s = raw_input().strip()
count =0
for char in s:
    if char.isupper():
        count = count +1
print (count +1)

