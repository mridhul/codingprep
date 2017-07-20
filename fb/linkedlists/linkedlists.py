class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
	def getdata(self):
		return self.data

def print_list(node):
	while node:
		print node.getdata()
		node = node.next

def insert(node,data):
	if node==None:
		return Node("randomNode",None)
	elif node.next==None:
		node.next=Node("RandomNode",None)
	else:
		insert(node.next,data)


n1 = Node("Node1")
#n2 = Node("Node2")
#n3 = Node("Node3")
#n1.next=n2
#n2.next=n3


insert(n1,"tester")
print_list(n1)