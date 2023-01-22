def combination_sum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

# The solution validated successfully on LeetCode
# https://leetcode.com/problems/combination-sum/submissions/883014524/
