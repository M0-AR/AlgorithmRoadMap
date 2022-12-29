# T: O(n) S: O(1)
def max_sub_array(nums):
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)

    return maxSub


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
