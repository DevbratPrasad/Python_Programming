def rsum (a,b):
    if(b==1):
        return a
    else:
        return a+rsum(a,b-1)
print("Multiplication= ",rsum(4,4))    
    
