def max_product_pair(nums):
    max_product = float("-inf")
    pair = ()
    s = set(nums)
    lst = list(s)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = lst[i] * lst[j]
            if product > max_product:
                max_product = product
                pair = (lst[i], lst[j])
    return pair, max_product

nums = [1, 7, 3, 9, 2, 10]
print("Max product pair:", max_product_pair(nums))
