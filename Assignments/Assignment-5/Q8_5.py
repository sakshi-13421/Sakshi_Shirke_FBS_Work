no = int(input("enter a no : "))
sum = 0

for i in range(1 ,11):
    sum += (no ** i ) / i

print(f"Sum of Series : ", sum)