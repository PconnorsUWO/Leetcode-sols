def smallestNumber(pattern: str) -> str:
    result = []
    num_stack = []

    for index in range(len(pattern) + 1):
        num_stack.append(index + 1)

        if index == len(pattern) or pattern[index] == "I":
            while num_stack:
                result.append(str(num_stack.pop()))

    return "".join(result)



# Input: pattern = "IIIDIDDD"
# Output: "123549876"
# Explanation:
# At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
# At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
# Some possible values of num are "245639871", "135749862", and "123849765".
# It can be proven that "123549876" is the smallest possible num that meets the conditions.
# Note that "123414321" is not possible because the digit '1' is used more than once.
# Example 2:
case1 =  "DDDDDDI"
print(smallestNumber(case1))
# Input: pattern = "DDD"
# Output: "4321"
# Explanation:
# Some possible values of num are "9876", "7321", and "8742".
# It can be proven that "4321" is the smallest possible num that meets the conditions.