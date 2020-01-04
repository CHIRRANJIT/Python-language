# Python3 code to demonstrate insert 
# operation in binary search tree 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None

# A utility function to 
# do inorder traversal of BST 
def inorder(root): 
	if root != None: 
		inorder(root.left) 
		print(root.key, end = " ") 
		inorder(root.right) 
		
# reverse tree path using queue 
def reversePath(node, key, q1): 
	
	# If the tree is empty, 
	# return a new node */ 
	if node == None: 
		return

	# If the node key equal 
	# to key then 
	if node.key == key: 
		
		# push current node key 
		q1.insert(0, node.key) 

		# replace first node 
		# with last element 
		node.key = q1[-1] 

		# remove first element 
		q1.pop() 

		# return 
		return
	
	# if key smaller than node key then 
	elif key < node.key: 
		
		# push node key into queue 
		q1.insert(0, node.key) 

		# recusive call itself 
		reversePath(node.left, key, q1) 

		# replace queue front to node key 
		node.key = q1[-1] 

		# performe pop in queue 
		q1.pop() 
	
	# if key greater than node key then 
	elif (key > node.key): 
		
		# push node key into queue 
		q1.insert(0, node.key) 

		# recusive call itself 
		reversePath(node.right, key, q1) 

		# replace queue front to node key 
		node.key = q1[-1] 

		# performe pop in queue 
		q1.pop() 

	# return 
	return
	
# A utility function to insert 
#a new node with given key in BST */ 
def insert(node, key): 
	
	# If the tree is empty, 
	# return a new node */ 
	if node == None: 
		return Node(key) 

	# Otherwise, recur down the tree */ 
	if key < node.key: 
		node.left = insert(node.left, key) 
	elif key > node.key: 
		node.right = insert(node.right, key) 

	# return the (unchanged) node pointer */ 
	return node 
	
# Driver Code 
if __name__ == '__main__': 
	
	# Let us create following BST 
	#			 50 
	#		 /	 \ 
	#		 30	 70 
	#		 / \ / \ 
	#	 20 40 60 80 */ 
	root = None
	q1 = [] 

	# reverse path till k 
	k = 80; 
	root = insert(root, 50) 
	insert(root, 30) 
	insert(root, 20) 
	insert(root, 40) 
	insert(root, 70) 
	insert(root, 60) 
	insert(root, 80) 

	print("Before Reverse :") 
	
	# print inoder traversal of the BST 
	inorder(root) 

	# reverse path till k 
	reversePath(root, k, q1) 
	print() 
	print("After Reverse :") 

	# print inorder of reverse path tree 
	inorder(root)	 
	

