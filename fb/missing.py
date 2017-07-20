def find_missing_number(list_numbers):
    for i in xrange(1,10):
        if i in list_numbers:
            pass
        else:
            print i

list_numbers=[1, 2, 4, 5, 6, 7, 8, 9, 10]
find_missing_number(list_numbers)