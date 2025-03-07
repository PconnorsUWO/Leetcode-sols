from typing import List
from collections import Counter

def generatePalindromes(s: str) -> List[str]:
    count = Counter(s)
    res = []
    
    mid = ""
    half = []
    for char, freq in count.items():
        if freq % 2 == 1:
            if mid:  
                return []
            mid = char
        half.extend([char] * (freq // 2))
    
    half.sort()
    
    def backtrack(path: List[str], used: List[bool]):
        if len(path) == len(half):
            half_str = ''.join(path)
            res.append(half_str + mid + half_str[::-1])
            return
        for i in range(len(half)):
            if used[i]:
                continue

            if i > 0 and half[i] == half[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(half[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    used = [False] * len(half)
    backtrack([], used)
    return res

# Example usage:
if __name__ == "__main__":
    test_string = "aabb"
    print(generatePalindromes(test_string))  # Output: ['abba', 'baab']

# Example 1:
case1 = "aabb"
print(generatePalindromes(case1))
# Input: s = "aabb"
# Output: ["abba","baab"]
# Example 2:

# Input: s = "abc"
# Output: []