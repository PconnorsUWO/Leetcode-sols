def q1(s,k):
    return any(len(list(grp)) == k for _, grp in groupby(s))



case1 = ["aaabaaa",  3]
print(q1(*case1))

    # Input: s = "aaabaaa", k = 3

# Output: true

# Explanation:

# The substring s[4..6] == "aaa" satisfies the conditions.

# It has a length of 3.
# All characters are the same.
# The character before "aaa" is 'b', which is different from 'a'.
# There is no character after "aaa".
# Example 2:

# Input: s = "abc", k = 2

# Output: false

# Explanation: