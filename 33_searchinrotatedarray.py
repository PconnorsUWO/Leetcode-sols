def search(nums, target):
    N = len(nums)
    left , right = 0 , N - 1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1



#Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
case1 = [4,5,6,7,0,1,2]
print(search(case1,4))
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1