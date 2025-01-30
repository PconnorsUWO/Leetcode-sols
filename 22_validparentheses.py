from typing import List
def generateParenthesis(n: int) -> List[str]:
    if n == 1:
        return ["()"]
    s = ""
    res = []

    def backtrack(s, left, right):
        if len(s) == 2*n:
            res.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)
    backtrack(s, 0, 0)
    return res

# O(4^n/sqrt(n)) time complexity, where n is the input n
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

case1 = 3
print(generateParenthesis(case1))