Side1=int(input("Enter a side1 : "))
Side2=int(input("Enter a side2 : "))
Side3=int(input("Enter a side3 : "))

if(Side1 == Side2 == Side3):
    print("Eqilateral Traingle")
elif(Side1 == Side2 or Side2 == Side3 or Side1 == Side3):
    print("Isosceles Traingle")
else:
    print("Scalena Traingle")
    
