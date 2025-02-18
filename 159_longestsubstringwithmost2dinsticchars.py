from collections import defaultdict
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n < 3:
        return n

    left, right = 0, 0

    hashmap = defaultdict()

    max_len = 2

    while right < n:
        hashmap[s[right]] = right
        right += 1

        if len(hashmap) == 3:
            del_idx = min(hashmap.values())
            del hashmap[s[del_idx]]
            left = del_idx + 1

        max_len = max(max_len, right - left)

    return max_len


# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:
case1 = "eceba"
print(lengthOfLongestSubstringTwoDistinct(case1))
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
 