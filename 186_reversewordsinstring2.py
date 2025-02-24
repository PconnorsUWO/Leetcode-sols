from typing import List
def reverseWords(s: List[str]) -> None:
    start = 0
    end = len(s) - 1
    while start < end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1

# Example 1:
case1 = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(reverseWords(case1))
# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Example 2:
# Input: s = ["a"]
# Output: ["a"]