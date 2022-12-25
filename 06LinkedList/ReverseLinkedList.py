# T: O(n) M: O(1)
def reverse_linked_list(head):
    prev, curr = None, head

    while curr:
        temp = curr
        curr = curr.next
        temp.next = prev
        prev = temp

    return prev


# The solution validated successfully on LeetCode
# https://leetcode.com/problems/reverse-linked-list/submissions/865143428/

# Using recursion
# T: O(n) M: O(n)
def reverse_linked_list_by_recursion(head):
    if not head:
        return head

    if not head.next:
        return head

    newHead = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return newHead

# The solution validated successfully on LeetCode
# https://leetcode.com/problems/reverse-linked-list/submissions/865154416/