def bubblesort(alist):

    isSorted = False
    count = 0
    while(not isSorted):
        isSorted=True
        arrlen = len(alist) -1

        for i in xrange(arrlen):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                isSorted=False
                count = count +1
                arrlen = arrlen -1

    print "Array sorted in {} swaps".format(count)
    print "First elemet: {}".format(alist[0])
    print "Last Element: {}".format(alist[len(alist) -1])

n = int(raw_input().strip())
alist = list(map(int, raw_input().strip().split(' ')))
bubblesort(alist)


#alist=[5,4,1,2,9]
#bubblesort(alist)
#print alist