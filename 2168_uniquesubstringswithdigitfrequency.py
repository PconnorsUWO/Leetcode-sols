from collections import Counter
import math
def equalDigitFrequency(s):
    unique_substrings = set()
    
    for i in range(len(s)):
        freq = Counter()
        for j in range(i, len(s)):
            freq[s[j]] += 1
            
            if len(set(freq.values())) == 1:
                unique_substrings.add(s[i:j+1])
    
    return len(unique_substrings)


# Example 1:

# Input: s = "1212"
# Output: 5
# Explanation: The substrings that meet the requirements are "1", "2", "12", "21", "1212".
# Note that although the substring "12" appears twice, it is only counted once.
# Example 2:
case1 = "1212"
print(equalDigitFrequency(case1))
# Input: s = "12321"
# Output: 9
# Explanation: The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".
 

# s = "12221"
# ["1","2","12","21","1221"]