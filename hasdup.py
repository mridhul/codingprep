def hasdup(alist):
	templist = []
	hasDuplicates = False
	for i in alist:
		if i not in templist:
			templist.append(i)
		else:
			hasDuplicates = True
	print templist
	return(hasDuplicates)





alist = [1,2,3,4,5,7,9]
print hasdup(alist)