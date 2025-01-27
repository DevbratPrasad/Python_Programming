n=int(input("Enter a value: "))
i=1
while(i<=n):
    if(i%2==0):
        j=1
        while(j<=i):
           print("*",end=" ")
           j=j+1
    else:
        j=1
        while(j<=i):
            print(j, end=" ")
            j=j+1
    print()
    i=i+1
    
