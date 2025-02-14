from typing import List
def permuteUnique(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort() 
    
    def backtrack(path, left):
        if not left:
            res.append(path)
            return
        for i in range(len(left)):
            if i > 0 and left[i] == left[i-1]:
                continue
            backtrack(path + [left[i]], left[:i] + left[i+1:])
    
    backtrack([], nums)
    return res

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
case1 = [1,1,2]
print(permuteUnique(case1))
