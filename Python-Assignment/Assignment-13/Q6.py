def multiply_dict(d):
    result = 1
    for k in d:
        result *= d[k]
    return result

d = {1: 2, 2: 3, 3: 4}
print("Multiplication of values:", multiply_dict(d))
