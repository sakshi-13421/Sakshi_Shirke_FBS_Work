def second_largest(lst):
    largest = lst[0]
    second = lst[0]

    for i in lst:
        if i > largest:
            largest = i

    for i in lst:
        if i != largest:   
            if i > second:
                second = i
    return second


numbers = [12, 35, 1, 10, 34, 1, 35]
print("Original List:", numbers)
print("Second Largest Element:", second_largest(numbers))
