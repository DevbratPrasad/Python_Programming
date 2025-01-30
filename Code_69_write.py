a=open("number.txt","w")
a.write("1 2 3 4 5 6 7 8 9 10")
a.close()
a=open("number.txt","rt")
b=open("numbet.txt","at")
c=open("number.txt","at")
for i in range (11):
    if (a.write(i)%2==0):
        b.write(i)
    else:
        c.write(i)
a.close()
b.close()
c.close()
    

