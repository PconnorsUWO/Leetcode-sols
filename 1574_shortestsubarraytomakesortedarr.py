def guess():
    return -1

def guessNumber(n: int) -> int:
    res = 0
    def recurse(low,high):
        nonlocal res
        cur_guess = (low + high) // 2
        res += cur_guess
        if cur_guess == high:
            return
        else:
            return recurse(cur_guess + 1, high)
    recurse(1,n)
    return res//2
 

# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:
print(guessNumber(10))
# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1