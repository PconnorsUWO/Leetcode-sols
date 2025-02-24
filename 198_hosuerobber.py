from typing import List
def rob(nums: List[int]) -> int:
    N = len(nums)
    dp = [None for _ in range(N + 1)]
    dp[N-1], dp[N] = nums[N-1], 0
    for i in range(N - 2,-1,-1):
        dp[i] = max(dp[i + 1], nums[i] + dp[i+2])
    return dp[0]

# Input: nums = [1,2,3,1]
# Output: 4

print(rob([1,2,3,1]))