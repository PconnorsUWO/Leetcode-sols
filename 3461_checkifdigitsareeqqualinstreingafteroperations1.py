def hasSameDigits(s: str) -> bool:
    while len(s) > 2:
        new_s = ''
        for i in range(len(s) - 1):
            digit1 = ord(s[i]) - ord('0')
            digit2 = ord(s[i + 1]) - ord('0')
            ch = str((digit1 + digit2) % 10)
            new_s += ch

        s = new_s

    return s[0] == s[1]

# Input: s = "3902"
case1 = "3902"
print(hasSameDigits(case1))
# Output: true