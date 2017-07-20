
word = str(raw_input())
print "You entered : ",word

if word[0] in 'aeiou':
	print "Modified: ",word[1:]+word[0]
