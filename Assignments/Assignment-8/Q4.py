def sum_of_odd(n):
    total = 0
    for i in range(1, n+1):
        if (i % 2 != 0):   
            total += i
    return total

n = int(input("Enter a number: "))
result = sum_of_odd(n)
print("Sum of odd numbers between 1 to", n, "is:", result) 
