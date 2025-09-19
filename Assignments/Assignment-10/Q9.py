n = int(input("Enter the number of elements in the list: "))

numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Original list:", numbers)
print("Even numbers list:", even_numbers)
print("Odd numbers list:", odd_numbers)
