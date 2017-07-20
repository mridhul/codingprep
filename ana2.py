#a = input().strip()
#b = input().strip()
#print(sum(abs(a.count(i) - b.count(i)) for i in 'abcdefghijklmnopqrstuvwxyz'))

a = 'abcde'
b = 'cdefg'

for i in 'abcdefghijklmnopqrstuvwxyz':
   print abs(a.count(i) - b.count(i))