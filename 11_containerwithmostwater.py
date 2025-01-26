from typing import List
def maxArea(height: List[int]) -> int:
    if len(height) == 2:
        return min(height[0], height[1])
    
    length = len(height)
    max_area = 0
    left = 0
    right = length - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

case1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(case1)) # 49

s = "hello"
print(len(s))