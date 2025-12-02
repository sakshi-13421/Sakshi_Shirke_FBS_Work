sub1=int(input("Enter marks of sub1 : "))
sub2=int(input("Enter marks of sub2 : "))
sub3=int(input("Enter marks of sub3 : "))
sub4=int(input("Enter marks of sub4 : "))
sub5=int(input("Enter marks of sub5 : "))

Total_Marks= sub1 + sub2 + sub3 + sub4 + sub5
Percentage= (Total_Marks/500)*100

if(Percentage >= 85):
    print("Distinct Class")
elif(Percentage >= 65):
    print("First Class")
elif(Percentage >= 45):
    print("Second Class")
elif(Percentage >= 35):
    print("Third Class")
else:
    print("Fail")

print(f"Percentage is {Percentage}")