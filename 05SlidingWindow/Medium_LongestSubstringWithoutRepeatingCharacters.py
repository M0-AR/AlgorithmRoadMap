def longest_substring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)

    return res


print(longest_substring("abcabcbb"))  # Output: 3
print(longest_substring("bbbbb"))     # Output: 1
print(longest_substring("pwwkew"))    # Output: 3
