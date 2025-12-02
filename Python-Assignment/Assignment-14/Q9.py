def three_sum(nums, target):
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return result

nums = [1, 2, -1, 0, -2, 3]
target = 2
print("Unique triplets:", three_sum(nums, target))
