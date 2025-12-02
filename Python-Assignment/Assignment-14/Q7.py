def missing_numbers(s1, s2):
    missing_in_s2 = set()
    missing_in_s1 = set()
    for x in s1:
        if x not in s2:
            missing_in_s2.add(x)
    for x in s2:
        if x not in s1:
            missing_in_s1.add(x)
    return missing_in_s2, missing_in_s1

A = {1, 2, 3, 4, 5}
B = {3, 4, 6}
print("Missing in B:", missing_numbers(A, B)[0])
print("Missing in A:", missing_numbers(A, B)[1])
