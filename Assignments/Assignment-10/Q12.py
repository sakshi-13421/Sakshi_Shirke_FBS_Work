n = int(input("Enter the number of elements: "))

li = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    li.append(num)

squares = [num**2 for num in li]
cubes = [num**3 for num in li]

print("Numbers list:", li)
print("Squares list:", squares)
print("Cubes list:", cubes)
