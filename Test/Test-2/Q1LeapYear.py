year=int(input("Enter a year : "))

if(year % 4 == 0):
    print(f"{year} is Leap Year")
elif(year % 100 != 0):
    print(f"{year} is Not Leap Year")
elif(year % 400 == 0):
    print(f"{year} is Leap Year")
else:
    print(f"{year} is Not Leap Year")

    