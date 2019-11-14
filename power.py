# Python3 Program to find 
# whether a no is 
# power of two 
import math 

# Function to check 
# Log base 2 
def Log2(x): 
	if x == 0: 
		return false; 

	return (math.log10(x) /
			math.log10(2)); 

# Function to check 
# if x is power of 2 
def isPowerOfTwo(n): 
	return (math.ceil(Log2(n)) ==
			math.floor(Log2(n))); 

# Driver Code 
if(isPowerOfTwo(31)): 
	print("Yes"); 
else: 
	print("No"); 

if(isPowerOfTwo(64)): 
	print("Yes"); 
else: 
	print("No"); 
	
