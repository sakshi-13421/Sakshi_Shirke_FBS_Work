length=int(input("Enter a length="))
breadth=int(input("Enter a breadth="))
radius=int(input("Enter a radius="))

area = length*breadth+1/2*3.14*radius*radius
perimeter = 2*length+breadth+3.14*radius

print(f"Area of rec {area}")

print(f"Perimeter of rec {perimeter}")
