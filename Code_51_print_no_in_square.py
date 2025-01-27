n=int(input("Enter of n: "))
i=n
while(i>=1):
    j=i
    while(j>=1):
        print(i,end=" ")
        j=j-1
    k=2
    while(k<=((n-i)+1)):
        print(k,end=" ")
        k=k+1
    print()
    i=i-1
