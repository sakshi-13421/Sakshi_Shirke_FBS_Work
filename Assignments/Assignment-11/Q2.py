def merge_and_sort(list1, list2):
    merged = []  
    for i in range(len(list1)):
        merged = merged + [list1[i]]
    for i in range(len(list2)):
        merged = merged + [list2[i]]

    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:

                temp = merged[j]
                merged[j] = merged[j+1]
                merged[j+1] = temp

    return merged

list1 = [5, 2, 9]
list2 = [1, 7, 3]
result = merge_and_sort(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Merged and Sorted List:", result)
