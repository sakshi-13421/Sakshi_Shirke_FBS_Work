import math

a = float(input("Enter a value ="))
b = float(input("Enter b value ="))
c = float(input("Enter c value ="))

d =(b*b) - (4*a*c)

root1=(-b+ math.sqrt(d))/(2*a)
root2=(-b- math.sqrt(d))/(2*a)

print(f"Root 1 is {root1}")
print(f"Root 2 is {root2}")

