no = int (input("Enter a no : "))
temp = no
total = 0
while(no > 0):
    digit = no % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    no //= 10
if(total == temp):
    print(f"{temp} is a strong number.")
else:
    print(f"{temp} is not a strong number.")
