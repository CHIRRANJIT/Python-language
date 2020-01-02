# Python program to find maximum product of two 
# non-intersecting paths 

# Returns maximum length path in subtree rooted 
# at u after removing edge connecting u and v 
def dfs(g, curMax, u, v): 
	
	# To find lengths of first and second maximum 
	# in subtrees. currMax is to store overall 
	# maximum. 
	max1 = 0
	max2 = 0
	total = 0

	# loop through all neighbors of u 
	for i in range(len(g[u])): 
		
		# if neighbor is v, then skip it 
		if (g[u][i] == v): 
			continue

		# call recursively with current neighbor as root 
		total = max(total, dfs(g, curMax, g[u][i], u)) 

		# get max from one side and update 
		if (curMax[0] > max1): 
			max2 = max1 
			max1 = curMax[0] 
		else: 
			max2 = max(max2, curMax[0]) 

	# store total length by adding max 
	# and second max 
	total = max(total, max1 + max2) 

	# update current max by adding 1, i.e. 
	# current node is included 
	curMax[0] = max1 + 1
	return total 

# method returns maximum product of length of 
# two non-intersecting paths 
def maxProductOfTwoPaths(g, N): 
	res = -999999999999
	path1, path2 = None, None

	# one by one removing all edges and calling 
	# dfs on both subtrees 
	for i in range(N): 
		for j in range(len(g[i])): 
			
			# calling dfs on subtree rooted at 
			# g[i][j], excluding edge from g[i][j] 
			# to i. 
			curMax = [0] 
			path1 = dfs(g, curMax, g[i][j], i) 

			# calling dfs on subtree rooted at 
			# i, edge from i to g[i][j] 
			curMax = [0] 
			path2 = dfs(g, curMax, i, g[i][j]) 

			res = max(res, path1 * path2) 
	return res 

# Utility function to add an undirected edge (u,v) 
def addEdge(g, u, v): 
	g[u].append(v) 
	g[v].append(u) 

# Driver code 
if __name__ == '__main__': 
	edges = [[1, 8], [2, 6], [3, 1], [5, 3], [7, 8], [8, 4], [8, 6]] 
	N = len(edges) 

	# there are N edges, so +1 for nodes and +1 
	# for 1-based indexing 
	g = [[] for i in range(N + 2)] 
	for i in range(N): 
		addEdge(g, edges[i][0], edges[i][1]) 
	print(maxProductOfTwoPaths(g, N)) 
