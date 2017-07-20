def duplicate_items(list_numbers):
    ret_list=[]
    list_numbers.sort() 							# O(n log(n)) - avg and O(n^2) - worst case
    for i in xrange(len(list_numbers) -1):			# O(n) - Linearly with the size of array
        if list_numbers[i]==list_numbers[i+1]:
        	ret_list.append(alist[i])
    return[ret_list]

alist=[1,5,2,7,8,55]

print duplicate_items(alist)