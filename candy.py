#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
c = map(int, raw_input().strip().split(' '))
# your code goes here
time =1
fixedN = n
toFillF = 0
while time <= t:
    for i in xrange(len(c)):

        n = n - c[i]
        if n < 5:
            toFill = (fixedN - 4)
            print "you need to fill ", toFill
            n = n + toFill
            #toFillF = toFillF + toFill
            #print "time to fill"
        print "time", time,n
        time = time +1
