def remove_key(d, key):
    new_dict = {}
    for k in d:
        if k != key:
            new_dict[k] = d[k]
    return new_dict

d = {1: "A", 2: "B", 3: "C"}
k = int(input("Enter key to remove: "))
print("After removal:", remove_key(d, k))
