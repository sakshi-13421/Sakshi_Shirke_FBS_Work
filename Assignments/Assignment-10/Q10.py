li = [10, 25, 7, 42, 25, 18, 25]

element = int(input("Enter the element to remove: "))

li = [num for num in li if num != element]

print("List after removing all occurrences of", element, ":", li)
