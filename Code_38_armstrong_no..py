#Wap to check armstrong number.
n=int(input("Enter the number: "))
s=0
t=n
while(n>0):
    d=n%10
    s=(s+d*d*d)
    n=n//10
if(t==s):
    print(t,"is an armstrong number")
else:
    print(t,"is not an armstrong number")
    
    

