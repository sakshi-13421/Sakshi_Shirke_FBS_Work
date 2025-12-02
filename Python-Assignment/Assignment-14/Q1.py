def difference_set(s1, s2):
    result = set()
    for x in s1:
        if x not in s2:
            result.add(x)
    return result

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Elements in A not in B:", difference_set(A, B))
