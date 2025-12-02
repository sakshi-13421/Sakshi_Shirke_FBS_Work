def generate_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i * i
    return d

n = int(input("Enter n: "))
print("Generated dictionary:", generate_dict(n))
