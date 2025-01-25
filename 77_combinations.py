from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    res = []
    def backtrack(index, path):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n + 1):
            backtrack(i + 1, path + [i])
    
    backtrack(1, [])
    return res

case1 = 4, 2
print(combine(*case1))