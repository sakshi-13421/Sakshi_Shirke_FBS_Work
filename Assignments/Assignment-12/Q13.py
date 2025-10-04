def count_digits_letters(string):
    digit = 0
    letter = 0
    for ch in string:
        if ch >= '0' and ch <= '9':
            digit += 1
        elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            letter += 1
    return digit, letter

s = input("Enter a string: ")
d, l = count_digits_letters(s)
print("Digits:", d)
print("Letters:", l)
