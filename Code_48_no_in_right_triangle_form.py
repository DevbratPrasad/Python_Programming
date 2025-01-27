n=int(input("Enter a value: "))
i=n
while(i>=1):
    j=n
    while(j>=i):
        print(j,end=" ")
        j=j-1
    print()
    i=i-1
