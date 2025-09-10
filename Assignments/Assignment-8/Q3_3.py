def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

# Main program
n = int(input("Enter a number: "))
print("Sum of series =", sum_of_powers(n))
