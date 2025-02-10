def myAtoi(s: str) -> int:
    MIN_INT = -2147483648
    MAX_INT = 2147483647
    
    s = s.strip()
    if not s:
        return 0
    
    isNegative = False
    if s[0] == '-':
        isNegative = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    res = 0
    for char in s:
        if not char.isdigit():
            break
        res = res * 10 + int(char)
    
    if isNegative:
        res = -res
    
    if res < MIN_INT:
        return MIN_INT
    if res > MAX_INT:
        return MAX_INT
    
    return res


# Example 1:

# Input: s = "42"

# Output: 42
# Explanation:
print("+".isnumeric())
case1 = " ++1"
print(myAtoi(case1))
case2 = "-+12"
print(myAtoi(case2))
case3 = "+-12"
print(myAtoi(case3))
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# Example 2:
case4 = "-+12"
print(myAtoi(case4))
# Input: s = " -042"

# Output: -42

# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#                ^
# Example 3:

# Input: s = "1337c0d3"

# Output: 1337

# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^
# Example 4:

# Input: s = "0-1"

# Output: 0

# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
# Example 5:

# Input: s = "words and 987"

# Output: 0

# Explanation:

# Reading stops at the first non-digit character 'w'.