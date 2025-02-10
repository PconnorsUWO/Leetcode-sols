def combinationSum2(candidates, target):
    candidates.sort()  
    res = []
    def backtrack(start, path, remain):
        if remain == 0:
            res.append(path.copy())  
            return
        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue 

            if candidates[i] > remain:
                break

            backtrack(i + 1, path + [candidates[i]], remain - candidates[i])

    backtrack(0, [], target)
    return res
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
case1 = [[10,1,2,7,6,1,5],8]
print(combinationSum2(*case1))