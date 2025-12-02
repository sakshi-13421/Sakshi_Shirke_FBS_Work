def separate_even_odd(lst):
    even_list = []  # list to store even numbers
    odd_list = []   # list to store odd numbers

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_list = even_list + [lst[i]] 
        else:
            odd_list = odd_list + [lst[i]]  

    return even_list, odd_list


numbers = [10, 15, 20, 25, 30, 35]
even_numbers, odd_numbers = separate_even_odd(numbers)

print("Original List:", numbers)
print("Even Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)
