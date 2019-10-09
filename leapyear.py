def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
y = int(input("Enter a year:"))
print(y,"is a leap year:",leap_year(y))
        
