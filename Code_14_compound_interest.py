principle=float(input("Enter the princilple amount: "))
rate=float(input("Enter the rate of interest(in %): "))
time=float(input("Enter  the time (in yrs): "))
compound_interest= principle * (1 + rate/100)**time - principle
print("Compound interest: ",compound_interest)
