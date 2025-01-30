# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted 
# from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

# Subtractive form
# If the value starts with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
# Normal Form
# Else select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result,


def intToRoman(num) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            thousands[num // 1000]
            + hundreds[num % 1000 // 100]
            + tens[num % 100 // 10]
            + ones[num % 10]
        )

# Input: num = 3
# Output: "III"
case1 = 3
print(intToRoman(case1))