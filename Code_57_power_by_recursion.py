def rpower(a,b):
    if(b==0):
        return 1
    else:
        return a * rpower(a,b-1)
#print("Power: ",rpower(3,2))
print("Power: ",rpower(int(input("Enter 1st no: ")),int(input("Enter 2nd no: "))))
