def toHex(num: int) -> str:
    if num == 0:
        return '0'
    if num < 0:
        num = (1 << 32) + num
    
    hex_digits = '0123456789abcdef'
    hex_num = ''

    while num > 0:
        digit = num % 16  
        hex_digit = hex_digits[digit] 
        hex_num = hex_digit + hex_num
        num //= 16
    
    return hex_num

# Example 1:
case1 = 26
print(toHex(case1))
# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"