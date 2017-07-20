class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next

	def getdata(self):
		return self.data


def printList(node):
	while node:
		print node.getdata()
		node = node.next

def addNode(head,data):
	if head is None:
		return(Node(data,None))
	elif head.next == None:
		head.next=Node(data,None)
	else:
		addNode(head.next,data)
	return head

opt=True
n1= Node("car")
#printList(n1)


while(opt):
	myOpt=int(raw_input("> "))
	if myOpt ==1:
		print "printing Linked List"
		printList(n1)
		print "====================="
	elif myOpt ==2:
		cData=str(raw_input("data> "))
		addNode(n1,cData)
	else:
		opt=False
