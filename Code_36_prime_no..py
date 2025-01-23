#Wap a program to print prime numbers.
n=int(input("Enter the number to check prime: "))
i=2
f=0
while(i<=n//2):
    if(n%i==0):
        f=1
    i=i+1
if(f==0):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

