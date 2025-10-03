def sort_by_length(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(lst[j]) > len(lst[j+1]):
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

list_of_strings = ["apple", "kiwi", "banana", "mangoes", "orange"]
sorted_list = sort_by_length(list_of_strings)

print("Original List:", list_of_strings)
print("List Sorted by Length:", sorted_list)
