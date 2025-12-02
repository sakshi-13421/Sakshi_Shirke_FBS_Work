def second_largest(lst):
    n = len(lst)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    
    return lst[n-2]

numbers = [10, 5, 20, 8, 15]
result = second_largest(numbers)

print("Original List:", [10, 5, 20, 8, 15])
print("Second Largest Number:", result)
