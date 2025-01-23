#percentage and grade in 5 subjects
sub1=int(input("Enter marks of sub1: "))
sub2=int(input("Enter marks of sub2: "))
sub3=int(input("Enter marks of sub3: "))
sub4=int(input("Enter marks of sub4: "))
sub5=int(input("Enter marks of sub5: "))
obtained_marks= sub1+sub2+sub3+sub4+sub5
print("Obtained marks by student are: ",obtained_marks)
total_marks=500
percentage=(obtained_marks/total_marks)*100
print("Percentage of student are: ",percentage)
if(percentage>=90<=100):
    print("A Grade")
elif(percentage>=75<=89):
    print("B Grade")
elif(percentage>=60<=77):
    print("C Grade")
elif(percentage>=40<=59):
    print("D Grades")
else:
    print("Failed")

