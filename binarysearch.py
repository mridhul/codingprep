def binarysearch(searchlist,target):

    found=False
    while found is False:

        end = len(searchlist) - 1
        middle = (0+end)/2
        print "Search area",searchlist,middle,target

        if target < middle:
            searchlist = searchlist[:middle]
            print "found at 1st half",searchlist
        elif target > middle:
            searchlist = searchlist[middle:]
            print "found at 2nd half", searchlist
        else:
            print "Found at ",searchlist[middle]
            found=True
        raw_input()

    else:
        print "Not found"


mylist=list(xrange(8))

binarysearch(mylist,4)
