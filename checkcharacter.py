ch=input("Enter a character")
ch=ord(ch)
if(ch>=65 and ch<=90):
    print("This is an UPPERCASE ALPHABET")
elif(ch>=97 and ch<=122):
    print("This is a LOWERCASE ALPHABET")
elif(ch>48 and ch<=57):
    print("This is a DIGIT")
else:
    print("This is a SPECIAL SYMBOL")
