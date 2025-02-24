import heapq as hq
from typing import List
def maxSum(grid: List[List[int]], limits: List[int], k: int) -> int:
    A = []
    for row, limit in zip(grid, limits):
        A += hq.nlargest(min(k, limit), row)
    return sum(hq.nlargest(k, A))

# Input: grid = [[1,2],[3,4]], limits = [1,2], k = 2

# Output: 7
case1 = [[1,2],[3,4]]
limits = [1,2]
k = 2
print(maxSum(case1,limits,k))
# Explanation:

# From the second row, we can take at most 2 elements. The elements taken are 4 and 3.
# The maximum possible sum of at most 2 selected elements is 4 + 3 = 7.
# Example 2:

# Input: grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3

# Output: 21