def remove_duplicates(lst):
    result = []  
    for item in lst:
        found = 0  
        for x in result:
            if x == item:
                found = 1  
                break
        if found == 0:
            result.append(item)
    return result

numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original List:", numbers)
print("List after removing duplicates:", remove_duplicates(numbers))
