def has_dup(alist):
	for i in xrange(len(alist) -1):
		for j in xrange(i+1,len(alist) -1):
			if alist[i] == alist[j]:
				return True
	return False


alist=[1,2,3,4,7,5]

print has_dup(alist)