def remove_element(lst, element):
    new_list = [] 
    for i in range(len(lst)):
        if lst[i] != element: 
            new_list = new_list + [lst[i]] 
    return new_list


numbers = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = int(input("Enter the element to remove: "))

result = remove_element(numbers, element_to_remove)
print("Original List:", numbers)
print("List after removing", element_to_remove, ":", result)
