# Brute force solution
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
print(three_sum_bf([0, 0, 0]))              # Output: [[0, 0, 0]]
print(three_sum_bf([-1, 0, 1]))             # [[-1, 0, 1]]