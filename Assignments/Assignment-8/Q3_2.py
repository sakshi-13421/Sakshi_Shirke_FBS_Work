def sum_of_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i      
        total += fact  
    return total

n = int(input("Enter a number: "))
print("Sum of factorials =", sum_of_factorials(n))
