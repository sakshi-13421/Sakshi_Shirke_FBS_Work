def sum_series(n):
    if n == 0:
        return 0
    return sum_series(n-1) + factorial(n)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

n = int(input("Enter no: "))
print(sum_series(n))