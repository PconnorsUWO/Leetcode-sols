def stringShift(s,shift):
    N = len(s)
    def shift_right(s, shift):
        return s[-shift:] + s[:-shift]
    def shift_left(s, shift):
        return s[shift:] + s[:shift]
    for direction, amount in shift:
        if direction == 0:
            s = shift_left(s, amount%N)
        else:
            s = shift_right(s, amount%N)
    return s


# Example 1:

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

case1 = "abc"
shift1 = [[0,1],[1,2]]
print(stringShift(case1,shift1))

# Example 2:
# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:  
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

case2 = "abcdefg"
shift2 = [[1,1],[1,1],[0,2],[1,3]]
print(stringShift(case2,shift2))
