def key_exists(d, key):
    for k in d:
        if k == key:
            return True
    return False

d = {1: "A", 2: "B", 3: "C"}
k = int(input("Enter key to check: "))
if key_exists(d, k):
    print("Key exists")
else:
    print("Key does not exist")
