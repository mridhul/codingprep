'''def quicksort(alist,start,end):
	if start < end:
		pivot = partition(alist,start,end)
		quicksort(alist,start,pivot -1)
		quicksort(alist,pivot +1,end)
	return alist

def partition(alist,start,end):
	pivot = alist[start]
	left = start +1
	right = end
	done = False

	while not done:
		while left <=right and alist[left] <=pivot:
			left = left + 1
		while alist[right] >= pivot and right >=pivot:
			right = right - 1
		if left <= right:
			done=True
		else:
			temp = alist[left]
			alist[right] = alist[left]
			alist[right] = temp
	## Swap right
	temp = alist[start]
	alist[start] = alist[right]
	alist[right] = temp
	return right'''

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

alist = [1,4,2,8,21,9,11]

quicksort(alist,0,6)

print alist


