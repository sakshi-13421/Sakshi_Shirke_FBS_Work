li = [10, 25, 30, 42, 60, 75, 90]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

divisible_numbers = [num for num in li if num % m == 0 and num % n == 0]

print(f"Numbers divisible by {m} and {n} are:", divisible_numbers)
