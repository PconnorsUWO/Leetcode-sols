from typing import List

def trap(height: List[int]) -> int:
    if len(height) == 0:
        return 0
    ans = 0
    size = len(height)
    left_max, right_max = [0] * size, [0] * size
    left_max[0] = height[0]
    for i in range(1, size):
        left_max[i] = max(height[i], left_max[i - 1])
    right_max[size - 1] = height[size - 1]
    for i in range(size - 2, -1, -1):
        right_max[i] = max(height[i], right_max[i + 1])
    for i in range(1, size - 1):
        ans += min(left_max[i], right_max[i]) - height[i]
    return ans

# 42. Trapping Rain Water
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
case1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(case1))
# Input: height = [4,2,0,3,2,5]
# Output: 9