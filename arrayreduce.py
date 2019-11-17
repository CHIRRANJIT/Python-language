# Function to return the minimum 
# operations required to reduce an array to zero
def minOperations(arr, n): 

	result = 0
	
	# Count the frequency of each element 
	freq = [0] * 1000001
	
	for i in range(0, n): 
		freq[arr[i]] += 1

	# Maximum element from the array 
	maxi = max(arr) 
	for i in range(1, maxi+1): 
		if freq[i] != 0: 

			# Find all the multiples of i 
			for j in range(i * 2, maxi+1, i): 

				# Delete the multiples 
				freq[j] = 0

			# Increment the operations 
			result += 1
		
	return result 

# Driver code 
if __name__ == "__main__": 

	arr = [2, 4, 2, 4, 4, 4] 
	n = len(arr) 

	print(minOperations(arr, n)) 
