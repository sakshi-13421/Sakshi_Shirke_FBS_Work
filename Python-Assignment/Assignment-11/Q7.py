def intersection_of_lists(list1, list2):
    intersection = []  

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:

                exists = 0
                for k in range(len(intersection)):
                    if intersection[k] == list1[i]:
                        exists = 1
                        break
                if exists == 0:
                    intersection = intersection + [list1[i]]
                break
    return intersection

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = intersection_of_lists(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Intersection of the two lists:", result)
