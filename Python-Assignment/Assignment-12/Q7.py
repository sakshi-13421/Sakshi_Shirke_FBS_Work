def string_length(string):
    count = 0
    for i in string:
        count = count + 1 
    return count

text = "Hello World"
length = string_length(text)
print("String:", text)
print("Length of the string:", length)
