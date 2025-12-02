def max_min(lst):
    max_val = lst[0]
    min_val = lst[0]
    
    for i in lst:
        if (i > max_val):
            max_val = i
        if (i < min_val):
            min_val = i            
    return max_val, min_val

numbers = [12, 5, 78, 34, 9, 8, 100]
maximum, minimum = max_min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
