def sum_of_primes(n):
    total = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            total += i
    return total

num = int(input("Enter a number: "))
res = sum_of_primes(num)
print("Sum of all prime numbers between 1 and", num, "is:", res)
