no = int(input("Enter a no : "))
sum = 0

for i in range(1, no + 1):
    sum += no ** i
print(f"Sum of Power is : ", sum)