def sort_by_second_element(lst):
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][1] > lst[j][1]:  
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst

list_of_sublists = [[1, 3], [2, 1], [4, 2], [3, 5]]
sorted_list = sort_by_second_element(list_of_sublists)

print("Original List:", [[1, 3], [2, 1], [4, 2], [3, 5]])
print("List Sorted by Second Element:", sorted_list)
