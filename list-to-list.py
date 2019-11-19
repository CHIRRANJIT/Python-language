# import the itertools 
import itertools 

# Declaring the list geek 
lt = [[1, 2], [3, 4], [5, 6]] 

# chain.from_iterable() function returns the elements of nested list 
# and iterate from first list of iterable till the last 
# end of the list 

lst = list(itertools.chain.from_iterable(lt)) 
print(lst)
