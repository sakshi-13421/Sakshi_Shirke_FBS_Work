def reverse_number(num):
    rev = 0
    while num != 0:
        digit = num % 10       
        rev = rev * 10 + digit 
        num //= 10             
    return rev


n = int(input("Enter a number: "))
print("Reverse of", n, "is:", reverse_number(n))
