def mysquare(x):
    return x**2
mylist = [10,11,12,13,14]
mob=map(mysquare, mylist)
mylist1 = list(mob)
print("Original List:", mylist)
print("New list: ",mylist1)
