numbers = [10, 25, 7, 42, 18, 25, 42, 10]

unique_numbers = list(set(numbers))
print("List without duplicates (method 1):", unique_numbers)

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List without duplicates (method 2, order preserved):", unique_numbers)
