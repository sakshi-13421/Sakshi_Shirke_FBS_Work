def sum_of_list(li):
    total = 0
    for element in li:
        total += element
    return total

list = [10, 20, 30, 40, 50] 
result = sum_of_list(list)
print("The sum of all elements in the list is:", result)
