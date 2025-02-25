from typing import List

def threeSumSmaller(nums: List[int], target: int) -> int:
    if len(nums) < 3:
        return 0
    count = 0
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count

# Input: nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation: Because there are two triplets which sums are less than 2:
# [-2,0,1]
# [-2,0,3]
case1 = [-2,0,1,3]
print(threeSumSmaller(case1, 2))