def find_single_number(nums):
    res = 0  # n ^ 0 = n
    for n in nums:
        res = n ^ res
    return res


print(find_single_number([2, 2, 1]))        # Output: 1
print(find_single_number([4, 1, 2, 1, 2]))  # Output: 4
