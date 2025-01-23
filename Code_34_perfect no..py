#Wap to print perfect number.
n=int(input("Enter a number to check perfect no.: "))
i=1
s=0
while(i<=n//2):
    if(n%i==0):
        s=s+i
    i=i+1
if(s==n):
    print(n,"is perfect number")
else:
    print(n,"is not a perfect number")
    
