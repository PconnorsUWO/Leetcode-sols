from typing import List
from collections import deque

def moveZeroes(nums: List[int]) -> None:
    last_non_zero_found_at = 0 

    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1



# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

case1 = [0,1,0,3,12]
moveZeroes(case1)

case2 = [0,0,1]
moveZeroes(case2)

print(case1)
print(case2)