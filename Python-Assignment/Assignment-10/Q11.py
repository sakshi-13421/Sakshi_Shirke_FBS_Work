def divisible_by_m_n(lst, m, n):
    result = [] 
    for i in range(len(lst)):
        if lst[i] % m == 0 and lst[i] % n == 0:
            result = result + [lst[i]] 
    return result

numbers = [10, 12, 15, 20, 24, 30, 36, 40]
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

result = divisible_by_m_n(numbers, m, n)
print("Original List:", numbers)
print("Numbers divisible by", m, "and", n, ":", result)
