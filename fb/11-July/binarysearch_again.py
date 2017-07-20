def binarysearch(alist,target):

	found = False
	while not found:
		mid = len(alist) -1 //2

		if target < alist[mid]:
			alist = alist[:mid]
		elif target > alist[mid]:
			alist = alist[mid:]
		else:
			print "found"
			found = True
			return(found)
	return False

