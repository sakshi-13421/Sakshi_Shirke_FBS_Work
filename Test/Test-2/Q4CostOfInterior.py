length=int(input("Enter a length = "))
breadth=int(input("Enter a breadth = "))
height=int(input("Enter a height = "))
rate=int(input("Enter a cost = "))

area = 2 * (length + breadth) * height
total_cost = area * rate

print(f"Total wall area : {area} sqm")
print(f"Total painting cost : rs {total_cost}")
