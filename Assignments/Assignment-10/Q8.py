def duplicate_list(lst):
    new_list = [] 
    for i in range(len(lst)):
        new_list = new_list + [lst[i]] 
    return new_list

original = [1, 2, 3, 4, 5]
copy_list = duplicate_list(original)

print("Original List:", original)
print("Copied List:", copy_list)

if id(original) != id(copy_list):
    print("Both lists are different objects.")
else:
    print("Both lists are pointing to the same object.")
