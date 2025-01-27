#Wap to create fibonacci series.
n=int(input("Enter the number: "))
i, j = 0, 1
k= i+j
print(i, j, end=",")
l=2
while(l<=n):
    print(k, end=",")
    i=j
    j=k
    k=i+j
    l=l+1
