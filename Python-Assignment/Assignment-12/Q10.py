def larger_string(str1, str2):
    
    len1 = 0
    for ch in str1:
        len1 += 1
    
    len2 = 0
    for ch in str2:
        len2 += 1
    
    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are of equal length"

string1 = "Hello"
string2 = "Python"
result = larger_string(string1, string2)
print("String 1:", string1)
print("String 2:", string2)
print("Larger string:", result)
