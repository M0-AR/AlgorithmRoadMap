# T: O(n*2^n) M: O(n) -> Recursion stack call
def subsets(nums):
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


print(subsets([1, 2, 3]))  # Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
