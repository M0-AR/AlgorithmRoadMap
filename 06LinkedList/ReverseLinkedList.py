# T: O(n) M: O(1)
def reverse_linked_list(head):
    prev, curr = None, head

    while curr:
        temp = curr
        curr = curr.next
        temp.next = prev
        prev = temp

    return prev

# The solution validated successfully by LeetCode
# https://leetcode.com/problems/reverse-linked-list/submissions/865143428/
