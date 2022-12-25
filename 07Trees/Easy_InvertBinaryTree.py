def invert_binary_tree(root):
    if not root:
        return None

    # swap
    root.right, root.left = root.left, root.right

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

# The solution validated successfully on LeetCode
# https://leetcode.com/problems/invert-binary-tree/submissions/865158559/
