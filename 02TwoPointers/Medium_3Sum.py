# Brute force solution
# T: O(n^3)
def three_sum_bf(nums):
    res = []
    nums_length = len(nums)

    for i in range(nums_length):
        for j in range(nums_length):
            for k in range(nums_length):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0 and i != j and i != k and j != k:
                    temp_list = sorted([nums[i], nums[j], nums[k]])
                    if temp_list not in res:
                        res.append(temp_list)

    return res


print(three_sum_bf([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, 0, 1], [-1, -1, 2]]
print(three_sum_bf([0, 0, 0]))  # Output: [[0, 0, 0]]
print(three_sum_bf([-1, 0, 1]))  # [[-1, 0, 1]]


# T: O(n^2) S: O(1) || O(n) # depend on sort library
def three_sum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:  # Move to next element if this element same as before
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, 0, 1], [-1, -1, 2]]
print(three_sum([0, 0, 0]))  # Output: [[0, 0, 0]]
print(three_sum([-1, 0, 1]))  # Output: [[-1, 0, 1]]
