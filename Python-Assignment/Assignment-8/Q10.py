def LeapYear(year):
    if(year % 4 == 0):
        return year

y=int(input("Enter a year : "))
if(LeapYear(y)):
    print(f"{y} is a leap year")
else:
    print(f"{y} is not a leap year")
