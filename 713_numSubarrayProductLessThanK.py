def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    total_count = 0
    product = 1

    left = 0
    for right, num in enumerate(nums):
        product *= num

        while product >= k:
            product //= nums[left]
            left += 1
        total_count += right - left + 1

    return total_count




# Input: nums = [10,5,2,6], k = 100
# Output: 8
case1 = [10,5,2,6]
print(numSubarrayProductLessThanK(case1,100))
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0