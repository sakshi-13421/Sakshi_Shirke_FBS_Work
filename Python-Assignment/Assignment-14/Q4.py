def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

nums = [2, 4, 3, 7, 5, 1]
target = 6
print("Pairs with sum", target, ":", find_pairs(nums, target))
