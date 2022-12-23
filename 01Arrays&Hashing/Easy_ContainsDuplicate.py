def contains_duplicate(nums) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)

    return False


print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3]))  # False
