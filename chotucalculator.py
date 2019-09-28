def calc(a,b):
    sum=a+b
    diff=a-b
    prod=a*b
    quotient=a/b
    return sum,diff,prod,quotient
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s,d,p,q=calc(a,b)
print("sum=",s)
print("Difference=",d)
print("Product=",p)
print("Quotient=",q)
