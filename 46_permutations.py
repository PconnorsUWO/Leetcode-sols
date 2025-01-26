def permute(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]
    
    res = []
    
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in nums:
            if i in path:
                continue
            backtrack(path + [i])

    backtrack([])
    return res
    