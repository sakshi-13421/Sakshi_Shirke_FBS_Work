def separate_even_odd(lst):
    even_list = [] 
    odd_list = []   

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_list = even_list + [lst[i]]  
        else:
            odd_list = odd_list + [lst[i]]   

    return even_list, odd_list

n = int(input("Enter number of elements in the list: "))
numbers = []

for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    numbers = numbers + [num] 

even_numbers, odd_numbers = separate_even_odd(numbers)

print("Original List:", numbers)
print("Even Numbers List:", even_numbers)
print("Odd Numbers List:", odd_numbers)
