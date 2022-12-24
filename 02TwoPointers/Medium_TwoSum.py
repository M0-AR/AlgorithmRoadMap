def two_sum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum > target:
            r -= 1
        else:
            l += 1

    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))  # Found
print(two_sum([2, 7, 11, 15], 5))  # Not found
