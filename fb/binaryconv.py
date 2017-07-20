def dec_to_bin(number):
	binList=[]
	while(number >= 1):
		rem = number % 2
		number = number //2
		binList.append(rem)
	print ''.join(str(e) for e in binList)

dec_to_bin(15)