def concat_dict(d1, d2):
    d3 = {}

    for k in d1:
        d3[k] = d1[k]

    for k in d2:
        d3[k] = d2[k]
    return d3

dict1 = {1: "A", 2: "B"}
dict2 = {3: "C", 4: "D"}
print("Concatenated dictionary:", concat_dict(dict1, dict2))
