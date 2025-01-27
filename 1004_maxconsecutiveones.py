def longestOnes(nums, k):
    l = 0
    for r in range(len(nums)):
        k -= 1 - nums[r]
        if k < 0:
            k += 1 - nums[l]
            l += 1
    return r - l + 1
        


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

case1 = [[1,1,1,1,1,1,1,0,0,0,1,1,1,1,0], 2]
case2 = [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]
print(longestOnes(*case1)) # 9
print(longestOnes(*case2)) # 10