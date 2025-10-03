def remove_even_numbers(lst):
    result = [] 
    for i in range(len(lst)):
        if lst[i] % 2 != 0:  
            result = result + [lst[i]]  
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = remove_even_numbers(numbers)

print("Original List:", numbers)
print("List after removing even numbers:", odd_numbers)
