n=int(input("Enter a value: "))
i=1
while(i<=n):
    j=1
    while(j<=i):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
        j=j+1
    print()
    i=i+1
