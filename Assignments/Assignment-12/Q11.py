def replace_space(string):
    result = ""
    for ch in string:
        if ch == " ":
            result += "-"
        else:
            result += ch
    return result

s = input("Enter a string: ")
print("Modified string:", replace_space(s))
