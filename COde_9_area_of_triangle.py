import math
a=float(input("Enter the first side of triangle:"))
b=float(input("Enter the second side of triangle:"))
c=float(input("Enter the third side of triangle:"))
perimeter = a+b+c
print("Perimeter of triangle is:",perimeter)
s=perimeter/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is:",area)
