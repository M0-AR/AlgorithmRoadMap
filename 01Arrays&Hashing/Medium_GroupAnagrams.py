from collections import defaultdict


# T: O(m * n) where m is the list of string is given and n is how many characters in each string
def sum_of_ascii(s):
    return sum(ord(c) for c in s)


def group_anagrams(strs):
    # Map every sum of word in ascii to list of Anagrams
    res = defaultdict(list)  # Avoid dealing with one edge case

    for s in strs:
        res[sum_of_ascii(s)].append(s)

    return res.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
