def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

num = int(input("Enter a number: "))
res = sum_n(num)
print("Sum from 1 to", num, "is:", res)
