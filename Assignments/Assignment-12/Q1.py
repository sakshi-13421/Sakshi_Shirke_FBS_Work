def replace_a_with_dollar(string):
    new_string = "" 
    for i in range(len(string)):
        if string[i] == 'a':
            new_string = new_string + '$'
        else:
            new_string = new_string + string[i]
    return new_string


text = "banana apple cat"
result = replace_a_with_dollar(text)

print("Original String:", text)
print("Modified String:", result)
