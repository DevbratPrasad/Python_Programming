#Wap a programme to print reverse of a number, calculate sum of digits, number of digits, check is its palindrom or not.
n=int(input("Enter the number to be reversed: "))
rev=0
m=n
sum=0
count=0
while(n>0):
    d=n%10
    n=n//10
    count=count+1
    sum=sum+d    
    rev=(rev*10+d)
print( "Reversed number is: ", rev)
print("Sum of digits:",sum)
print("Count of digits: ",count)
if(rev==m):
    print(m,"is palindrom")
else:
    print(m,"is not palindrom")

    
