# Python3 program to find the only 
# repeating element in an array where 
# elements are from 1 to n-1. 

def findRepeating(arr, n): 
	
	# Find array sum and subtract sum 
	# first n-1 natural numbers from it 
	# to find the result. 
	return sum(arr) -(((n - 1) * n) // 2) 

# Driver Code 
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7] 
n = len(arr) 
print(findRepeating(arr, n)) 
