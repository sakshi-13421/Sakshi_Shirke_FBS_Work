def remove_odd_index(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:  
            new_string = new_string + string[i]
    return new_string

text = "Python"
result = remove_odd_index(text)
print("Original String:", text)
print("String after removing odd index characters:", result)
