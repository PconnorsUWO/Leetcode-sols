def maxVowels(s: str, k: int):
    if len(s) < k:
        return 0
    
    vowels = set('aeiou')
    l, r = 0, k - 1
    cur_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            cur_vowels += 1
    max_vowels = cur_vowels
    while r < len(s) - 1:
        if s[l] in vowels:
            cur_vowels -= 1
        if s[r + 1] in vowels:
            cur_vowels += 1
        if max_vowels < cur_vowels:
            max_vowels = cur_vowels

        r += 1
        l += 1

    return max_vowels
case1 = ["abciiidef", 3]
case2 = ["aeiou", 2]
case3 = ["leetcode", 3]
print(maxVowels(*case1)) # 3
print(maxVowels(*case2)) # 2
print(maxVowels(*case3)) # 2

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.