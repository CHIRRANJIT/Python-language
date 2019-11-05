m1=[]
r1=int(input("Enter r1:"))
c1=int(input("Enter c1:"))
for i in range(r1):
    a=[]
    for j in range(c1):
        x=int(input("Enter item:"))
        a.append(x)
        m1.append(a)
        m2=[]
    for i in range(r1):
        b=[]
        for j in range(c1):
            x=int(input("Enter item:"))
            b.append(x)
            m2.append(b)
        r=[]
        for i in range(c1):
            a.append(a)
            r.append(a)
        for i in range(r1):
            for j in range(c1):
                for k in range(c1):
                    r[i][j]=r[i][j]+m1[i][k]*m2[k][j]
                    print("\n 1st matrix")
                    for i in m1:
                        print(i)
                    print("\n 2nd matrix")
                    for i in m2:
                        print(i)
                    print("\n Resultant matrix")
                    for l in r:
                        print(i)
