class Node:
	def __init__(self,data):
		self.right=self.left=None
		self.data = data

class Solution:
	def insert(self,root,data):
		if root == None:
			return (Node(data))
		elif data < root.data:
			cur = self.insert(root.left,data)
			root.left = cur
		else:
			cur = self.insert(root.right,data)
			root.right = cur
		return root

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
print myTree.root
#height=myTree.getHeight(root)
#print(height)