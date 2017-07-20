#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    winCount =0
    lostCount = 0
    for i in range(1,len(s)):
        maxC = max(s[0:i])
        minC = min(s[0:i])
        if s[i] > maxC:
            winCount+= 1
        if s[i] < minC:
            lostCount -= 1
    return winCount,lostCount

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))


