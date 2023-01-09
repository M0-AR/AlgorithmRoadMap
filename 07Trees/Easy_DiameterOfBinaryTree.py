from Easy_MaximumDepthOfBinaryTree import max_depth


# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
# T: O(n^2) S: O(n) for stack calling
def diameter0(root):
    if root is None:
        return -1

    # Get the height of left and right sub-trees
    lh = max_depth(root.left)
    rh = max_depth(root.right)

    # Get the diameter of left and right sub-trees
    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(lh + rh + 1, max(ld, rd))


# T: O(n) S: O(n) for stack calling
def diameter(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)

        return 1 + max(left, right)

    dfs(root)
    return res[0]
