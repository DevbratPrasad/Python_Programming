def rdiv(a,b):
    if(a<b):
        return 0
    else:
        return 1+rdiv(a-b,b)
#print("Division",rdiv(6,2))
print("Division: ",rdiv(int(input("First no: ")),int(input("Second no:"))))
