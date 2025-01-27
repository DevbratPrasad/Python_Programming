# Wap a programme to find Armstrong number with nested loop.
n=int(input("Enter the number: "))
i=1
while(i<=n):
    l=len(str(i))
    k=i
    s=0
    while(k>0):
        r=k%10
        s=s+r**l
        k=k//10
    if(i==s):
        print(i,"is Armstrong")
    #else:
        #print(i,"is not Armstrong")
    i=i+1
