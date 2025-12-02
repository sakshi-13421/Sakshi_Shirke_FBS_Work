def replace_spaces_with_hyphen(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == " ":
            new_string = new_string + "-"  
        else:
            new_string = new_string + string[i]  
    return new_string

text = "Hello World Python"
result = replace_spaces_with_hyphen(text)
print("Original String:", text)
print("Modified String:", result)
