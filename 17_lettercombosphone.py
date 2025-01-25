from typing import List

def letterCombinations(digits: str) -> List[str]:
    res = []
    
    if not digits:
        return res

    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return
        for letter in letters[digits[index]]:
            backtrack(index + 1, path + letter)
    
    backtrack(0, "")
    return res

case1 = "23"
print(letterCombinations(case1))