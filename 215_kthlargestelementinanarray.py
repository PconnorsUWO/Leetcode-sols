from typing import List
from heapq import heappush, heappop
def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heappush(heap,num)
        if len(heap) > k:
            heappop(heap)
    return heappop(heap)

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
case1 = [3,2,1,5,6,4]
print(findKthLargest(case1,2))

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
case2 = [3,2,3,1,2,4,5,5,6]
print(findKthLargest(case2,4))
 