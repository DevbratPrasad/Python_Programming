for i in range(1, 10):
    if(1>=4 and i<=6):
        continue
    print(i, end=" ")


print("by using while loop:")
i=0
while(i<=9):
    i=i+1
    if(i>=4 and i<=6):
        continue
    print(i,end=" ")
