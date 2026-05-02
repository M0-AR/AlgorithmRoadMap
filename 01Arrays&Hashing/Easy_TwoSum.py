def two_sum(nums, target):
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))  # Found
print(two_sum([2, 7, 11, 15], 5))  # Not found
