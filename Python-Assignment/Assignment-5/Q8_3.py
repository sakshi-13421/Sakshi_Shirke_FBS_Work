no = int(input("enter a no : "))
sum = 0
term = 1

for i in range(no):
    sum += term
    term *= 2

print(f"Geometric Series Sum : ", sum)