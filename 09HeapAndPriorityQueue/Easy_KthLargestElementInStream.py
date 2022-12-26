import heapq


# Stream: continuously adding a number to a list of number
class KthLargest:
    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)  # Will create a sorted property and run in O(n)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# The solution validated successfully on LeetCode
# https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/865762945/