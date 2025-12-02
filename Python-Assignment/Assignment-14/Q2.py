def remove_intersection(s1, s2):
    result = set()
    for x in s1:
        if x not in s2:
            result.add(x)
    return result

A = {1, 2, 3, 4}
B = {2, 3}
print("After removing intersection:", remove_intersection(A, B))
