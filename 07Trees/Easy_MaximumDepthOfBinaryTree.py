def max_depth(root):
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))

# The solution validated successfully on LeetCode
# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/874720835/
