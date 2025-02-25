from typing import List

def distinct_numbers(nums: List[int], k: int) -> List[int]:
    N = len(nums)
    res = []
    val_dict = {}

    for i in range(0,k):
        val_dict[nums[i]] = i
    res.append(len(val_dict.keys()))

    for i in range(k, N):
        cur_val = nums[i]
        if cur_val in val_dict:
            if i - val_dict[cur_val] + 1 > k:
                val_dict[cur_val] = i
                res.append(res[-1])
            else:
                val_dict[cur_val] = i
                res.append(res[-1] - 1)
        else:
            val_dict[cur_val] = i
            res.append([res[-1]])
    return res,val_dict

print(distinct_numbers(nums = [1,2,3,2,2,1,3], k = 3))