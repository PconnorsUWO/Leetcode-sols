from typing import List
def longestSubarray(nums: List[int]) -> int:
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        current_window_length = right - left
        max_len = max(max_len, current_window_length)

    return max_len


# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

case1 = [1,1,0,1]
print(longestSubarray(case1)) # 3