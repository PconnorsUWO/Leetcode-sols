from typing import List
# O(n^2) solution
# def maxOperations(nums: List[int], k: int) -> int:
#     operations = 0
#     paired = set()
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i == j or (i in paired or j in paired):
#                 continue
#             if nums[i] + nums[j] == k:
#                 operations += 1
#                 paired.add(i)
#                 paired.add(j)
#     return operations

def maxOperations(nums: List[int], k: int) -> int:
    operations = 0
    nums_map = {}
    for num in nums:
        if num in nums_map:
            nums_map[num] += 1
        else:
            nums_map[num] = 1
    for num in nums:
        if nums_map[num] > 0 and k - num in nums_map and nums_map[k - num] > 0:
            if num == k - num:
                if nums_map[num] < 2:
                    continue
            operations += 1
            nums_map[num] -= 1
            nums_map[k - num] -= 1
    return operations
case1 = [1,2,3,4]
case2 = [3,1,3,4,3]
print(maxOperations(case1, 5)) 
print(maxOperations(case2, 6))