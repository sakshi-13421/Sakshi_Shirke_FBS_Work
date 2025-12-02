def add_pair(d, key, value):
    d[key] = value  
    return d

my_dict = {1: "Apple", 2: "Banana"}
k = input("Enter key: ")
v = input("Enter value: ")
print("Updated dictionary:", add_pair(my_dict, k, v))
