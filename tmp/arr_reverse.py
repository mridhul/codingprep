#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
#prstring=""
for i in arr[::-1]:
	prstring=prstring+str(i)

print ' '.join(prstring)