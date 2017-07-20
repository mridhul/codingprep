
import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

maxVal = max(height)
absCount = 0
for i in xrange(len(height)):
    if height[i] == maxVal:
        absCount = absCount + 1

print absCount