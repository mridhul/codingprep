#s = int(raw_input().strip())
#for a0 in xrange(s):
#    n = int(raw_input().strip())

def climb(stairs,count):
    ways=0
    for i in range(1,stairs,count):
        ways = ways + i
        print i,ways
    return (ways)


print climb(1,1)