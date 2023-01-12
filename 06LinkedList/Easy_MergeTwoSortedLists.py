class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_list(list1, list2):
    res = ListNode()
    tail = res.next

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    while list1:
        tail.next = list1
        tail = tail.next
        list1 = list1.next

    while list2:
        tail.next = list2
        tail = tail.next
        list2 = list2.next

    return res.next

# The solution validated successfully on LeetCode
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/876768370/
