def remove_nth_char(string, n):
    new_string = "" 
    for i in range(len(string)):
        if i != n:  
            new_string = new_string + string[i]
    return new_string

text = "Python"
n = 3  
result = remove_nth_char(text, n)

print("Original String:", text)
print("String after removing index", n, ":", result)
