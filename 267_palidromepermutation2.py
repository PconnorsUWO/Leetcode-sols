from typing import List
from collections import Counter

def generatePalindromes(s: str) -> List[str]:
    count = Counter(s)
    N = sum(count.values())

    def canPermutePalindrome(counter_object: dict, length: int) -> bool:
        if length % 2 == 0:
            for i in count.values():
                if i % 2 != 0: return False
            return True
        else:
            odd = 0
            for i in count.values():
                if i % 2 == 1: 
                    odd += 1
                    if odd > 1:
                        return False
            return True
        
    def generate_permutations(s):
        if len(s) <= 1:
            return [s]
        perms = []
        for i, char in enumerate(s):
            for perm in generate_permutations(s[:i] + s[i+1:]):
                perms.append(char + perm)
        return perms

    if canPermutePalindrome(count, N):
        res = generate_permutations(s)
        return res
    
    else:
        return []
# Example 1:
case1 = "aabb"
print(generatePalindromes(case1))
# Input: s = "aabb"
# Output: ["abba","baab"]
# Example 2:

# Input: s = "abc"
# Output: []