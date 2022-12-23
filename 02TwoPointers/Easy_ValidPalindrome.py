# Time: O(n) - Space: O(n)
def is_palindrom(s) -> bool:
    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


print(is_palindrom("aabbaa"))  # True
print(is_palindrom("aaaccc"))  # False


def is_alphaNum(c) -> bool:
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


# Time: O(n) - Space: O(1)
def is_palindrom(s) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not is_alphaNum(s[l]):
            l += 1
        while r > l and not is_alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


print(is_palindrom("aabbaa"))  # True
print(is_palindrom("aaaccc"))  # False
