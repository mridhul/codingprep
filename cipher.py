#!/bin/python

import sys
import string


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
newarr = []

for char in s:
    if int(ord(char)) in range(97,122):
        if int(ord(char)+int(k)) in range(97,122):
            newarr.append(chr(ord(char)+int(k)))
        else:
            newarr.append(char(ord))

    else:
        newarr.append(char)


print ''.join(newarr)