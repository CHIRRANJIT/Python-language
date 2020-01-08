# Python3 code to print BST keys in given Range 
# in constant space using Morris traversal. 

# Helper function to create a new node 
class newNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Function to print the keys in range 
def RangeTraversal(root, n1, n2): 
	if root == None: 
		return

	curr = root 
	while curr: 
		if curr.left == None: 
			
			# check if current node lies 
			# between n1 and n2 
			if curr.data <= n2 and curr.data >= n1: 
				print(curr.data, end = " ") 
			curr = curr.right 
		else: 
			pre = curr.left 
			
			# finding the inorder predecessor- 
			# inorder predecessor is the right 
			# most in left subtree or the left 
			# child, i.e in BST it is the 
			# maximum(right most) in left subtree. 
			while (pre.right != None and
				pre.right != curr): 
				pre = pre.right 
						
			if pre.right == None: 
				pre.right = curr; 
				curr = curr.left 
			else: 
				pre.right = None

				# check if current node lies 
				# between n1 and n2 
				if curr.data <= n2 and curr.data >= n1: 
					print(curr.data, end = " ") 
				curr = curr.right 

# Driver Code 
if __name__ == '__main__': 

	# Constructed binary tree is 
	#	 4 
	#	 / \ 
	#	 2	 7 
	# / \ / \ 
	# 1 3 6 10 
	root = newNode(4) 
	root.left = newNode(2) 
	root.right = newNode(7) 
	root.left.left = newNode(1) 
	root.left.right = newNode(3) 
	root.right.left = newNode(6) 
	root.right.right = newNode(10) 

	RangeTraversal(root, 4, 12)	 
