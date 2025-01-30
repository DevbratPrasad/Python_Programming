#when entering alphabet with integer
try:
    num=int(input("Enter the numerator: "))
    num1=int(input("Enter the denominator: "))
    c=num/num1
    print(c)
except ZeroDivisionError :
    print("Don't enter zero for denominator")
except ValueError:
    print("Please enter numeric value")
finally:
    print("Execute always")
