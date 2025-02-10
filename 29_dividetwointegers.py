def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend
    if divisor == -1:
        if dividend == -2**31:
            return 2**31 - 1
        return -dividend
    if dividend == divisor:
        return 1
    if dividend == -divisor:
        return -1


    quotient = 0
    while dividend - divisor >= 0:
        quotient += 1
        dividend -= divisor
    
    return quotient

    # If there was originally one negative sign, then
    # the quotient remains negative. Otherwise, switch
    # it to positive.
# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:
case1= [10,3]
print(divide(*case1))
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
