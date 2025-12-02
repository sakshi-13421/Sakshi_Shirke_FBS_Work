def Palindrome(no):
    temp = no
    rev = 0

    # while(no > 0):
    digit = no % 10
    rev = rev * 10 + digit
    no = no // 10
    
    digit = no % 10
    rev = rev * 10 + digit
    no = no // 10

    digit = no % 10
    rev = rev * 10 + digit
    no = no // 10
    
    return temp == rev

no = int(input("Enter a no : "))
if(Palindrome(no)):
    print(f"{no} is Pallindrome number.")
else:
    print(f"{no} is not a Pallindrome number.")