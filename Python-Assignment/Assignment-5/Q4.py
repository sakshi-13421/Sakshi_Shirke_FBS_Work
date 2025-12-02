no = int(input("Enter a no : "))
sum = 0

temp = no
while(temp > 0):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if(no == sum):
    print(f"{no} is a armstrong number")
else:
    print(f"{no} is not a armstrong number")
