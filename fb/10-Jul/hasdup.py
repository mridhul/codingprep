def hasdup(alist):
	alist.sort()
	hasdupVal=False
	for i in xrange(len(alist) -1):
		if alist[i] == alist[i+1]:
			hasdupVal=True
	return hasdupVal

alist=[1,5,2,9,7,5]
print hasdup(alist)

