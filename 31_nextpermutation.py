from typing import List
import statistics as st

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]
        
        def reverse(start,arr):
            if len(arr) == 1:
                return
            l = start
            r = len(nums)-1
            while l < r:
                swap(l,r)
                l += 1
                r -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            swap(i, j)
        reverse(i+1,nums[i+1:])



# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
case1 = [1,2,3]
Solution.nextPermutation(Solution,case1)
print(case1[0+1:])

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5,3,6]
# Output: [1,3,1,5,6]
case2 = [1,1,5,3,6]
Solution.nextPermutation(Solution,case2)
print(case2)

