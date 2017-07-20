
f=open('test.txt','r')

for word in f.readlines():
	if word =="test":
		print "found"
