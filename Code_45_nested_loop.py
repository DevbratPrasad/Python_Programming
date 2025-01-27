n1= int(input("Enter n1: "))
n2= int(input("Enter n2: "))
i=1
while(i<=10):
    j=n1
    while(j<=n2):
        print(j,"*",i,"=",i*j,end=" ")
        j=j+1
    print()
    i=i+1
