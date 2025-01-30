cubes=[i**3 for i in range(11)]
print(cubes)

print([(x,y) for x in [10,20,30] for y in [30,10,40] if x!=y])

cubes=[i**3 for i in range (11) ]
print(cubes)

list=[3,6,4,7,9,7,3,7]
print(list)
sum=0
for i in list:
    sum=sum+i
print("sum of list: ",sum)
length=len(list)
print("mean of list:",sum/length)
