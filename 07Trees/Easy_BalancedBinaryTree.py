# TODO: there is a bug
def is_balanced(root):
    def dfs(node):
        if not node: return [True, 0]

        left, right = dfs(node.left), dfs(node.right)
        balanced = (left[0] and right[0] and
                    abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)

# The solution validated successfully on LeetCode
#
