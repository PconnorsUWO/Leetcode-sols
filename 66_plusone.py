from typing import List

def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    
    r = len(digits) - 1
    while digits[r] == 9:
        digits[r] = 0
        r -= 1
        if r < 0:
            digits.insert(0, 1)
            return digits
    digits[r] += 1
    return digits





case1 = [1,2,3]
case2 = [8,9,9,9]
case3 = [9,9,9,9]
print(plusOne(case1))
print(plusOne(case2))
print(plusOne(case3))
