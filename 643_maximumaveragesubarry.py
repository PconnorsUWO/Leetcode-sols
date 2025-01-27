def findMaxAverage(nums, k):
    l, r = 0, k
    max_sum = sum(nums[l:r])
    cur_sum = max_sum
    while r < len(nums):
        cur_sum += nums[r] - nums[l]
        if cur_sum > max_sum:
            max_sum = cur_sum
        l += 1
        r += 1
    
    return max(max_sum/k, sum(nums[l:r])/k)

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

case1 = [1,12,-5,-6,50,3]
k = 4
case2 = [[0,1,1,3,3], 4]
print(findMaxAverage(case1, k)) # 12.75
print(findMaxAverage(*case2)) # 2.0