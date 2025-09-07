no = int (input("Enter a no : "))
sum = 0
fact = 1

for i in range(1, no + 1):
    fact *= i
    sum += fact

print("Sum of Factorial is: ", sum)