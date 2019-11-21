# Function to check whether 
# the given number is duck number or not. 

def check_duck(num ) : 
	# Length of the number(number of digits) 
	l = len(num) 
	count_zero = 0
	i = 1
	while i < l : 
		# Checking for a digit whether it is a '0' or not 
		ch = num[i] 
		if(ch == "0") : 
			count_zero = count_zero + 1
		i = i + 1
	
	return count_zero 
	

# Driver Method 
num1 = "1023"

# Extracting the first digit 
first_digit1 = num1[0] 

# Checking number1 
if( check_duck(num1) > 0 and first_digit1 != '0') : 
	print ("It is a duck number")
else : 
	print ("It is not a duck number")
