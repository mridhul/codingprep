#!/bin/python

import sys

def solve(n, p):
    # Complete this function
    fromFront = 0
    fromBack = -1
    finArr = []
    for x in range(1,p):
        fromFront = fromFront +1
    finArr.append(fromFront)

    for x in range(n,p,-1):
        fromBack = fromBack +1
    if fromBack >= 0:
        finArr.append(fromBack)
    else:
        finArr.append(0)

    return min(finArr)

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)