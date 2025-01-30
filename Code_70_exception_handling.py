#if entering 0 in denominator
try:
    num=int(input("Enter the numerator: "))
    num1=int(input("Enter the denominator: "))
    c=num/num1
    print(c)
except ZeroDivisionError :
    print("Don't enter zero for denominator")
finally:
    print("Execute always")
