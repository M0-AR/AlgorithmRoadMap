def binary_search(nums, target):
    if not nums:
        return -1

    l, r = 0, len(nums) - 1

    while l < r:
        mid = (r + l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


print(binary_search([-1, 0, 3, 5, 9, 12], 9))  # 4
print(binary_search([-1, 0, 3, 5, 9, 12], 2))  # -1
