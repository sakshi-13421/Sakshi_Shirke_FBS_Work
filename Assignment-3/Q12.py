no=int(input("Enter a 3 digit no : "))

rev=(no % 10) * 100 + ((no // 10) % 10) * 10 + (no // 100)

if(no == rev):
    print(f"{no} is pallindrome number")
else:
    print(f"{no} is pallindrome number")
