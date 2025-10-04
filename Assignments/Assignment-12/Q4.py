def exchange_first_last(string):
    if len(string) <= 1:
        return string

    new_string = string[-1] + string[1:-1] + string[0]
    return new_string


text = "python"
result = exchange_first_last(text)

print("Original String:", text)
print("String after exchanging first and last characters:", result)
