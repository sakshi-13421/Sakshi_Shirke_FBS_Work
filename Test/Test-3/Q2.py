no = int (input("Enter a no : "))
total = 0

for i in range(1, no + 1):
    
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    total += (i ** i) / fact

print("Sum of series is: ", total)