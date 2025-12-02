def larger_string(str1, str2):
    len1 = 0
    len2 = 0

    # length manually काढणे
    for _ in str1:
        len1 += 1
    for _ in str2:
        len2 += 1

    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are equal length"

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Larger string is:", larger_string(s1, s2))
