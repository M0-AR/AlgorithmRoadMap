# T: O(n) S: O(n)
def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    # Count how many times does the value occurred
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # Append n to list at c index, where n occur c amount of times
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
print(topKFrequent([1], 1))  # Output: [1]
