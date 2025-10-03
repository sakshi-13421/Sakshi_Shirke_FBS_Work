def union_of_lists(list1, list2):
    union_list = list1  

    for i in range(len(list2)):
        exists = 0
        for j in range(len(union_list)):
            if list2[i] == union_list[j]:
                exists = 1
                break
        if exists == 0:
            union_list = union_list + [list2[i]]

    return union_list

list1 = [1, 2, 3]
list2 = [3, 4, 5]
result = union_of_lists(list1, list2)

print("Union of the two lists:", result)
