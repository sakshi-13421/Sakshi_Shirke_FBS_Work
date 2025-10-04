def count_lowercase(string):
    count = 0
    for ch in string:
        if ch >= 'a' and ch <= 'z':
            count += 1
    return count

s = input("Enter a string: ")
print("Lowercase letters count:", count_lowercase(s))
