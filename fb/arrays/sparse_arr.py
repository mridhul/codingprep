
n=int(raw_input())
strArr=[]

for i in xrange(n):
	strArr.append(raw_input())

q=int(raw_input("Q> "))
for i in xrange(q):
	quer=raw_input()
	matching=[s for s in strArr if quer in s]
	print len(matching)