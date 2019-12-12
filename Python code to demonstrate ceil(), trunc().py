# Python code to demonstrate ceil(), trunc() 
# and floor() 

# importing "math" for precision function 
import math 

# initializing value 
a = 3.4536

# using trunc() to print integer after truncating 
print ("The integral value of number is : ",end="") 
print (math.trunc(a)) 

# using ceil() to print number after ceiling 
print ("The smallest integer greater than number is : ",end="") 
print (math.ceil(a)) 

# using floor() to print number after flooring 
print ("The greatest integer smaller than number is : ",end="") 
print (math.floor(a)) 
