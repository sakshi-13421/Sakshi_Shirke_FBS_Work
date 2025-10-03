def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1): 
        rev.append(lst[i])
    return rev

numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
print("Reversed List:", reverse_list(numbers))
