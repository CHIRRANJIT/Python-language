max = lambda x,y:x if x > y else y    # LAMBDA FUNCTION
a,b = [int (n) for n in input("ENTER TWO NUMBER").split(',')]
print("Bigger Number =",max(a,b))
