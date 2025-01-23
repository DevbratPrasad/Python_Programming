#Wap to find factorial of a number.
n=int(input("Enter the number to find factorial: "))
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
print("factorial is: ",fact)    
