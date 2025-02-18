def isOneEditDistance(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False
    dif_count = 0
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]:
            dif_count += 1
    if dif_count == 2 or ((abs(len(s) - len(t))) == 1 and dif_count == 1):
        print(dif_count)
        return False
    return True


# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:
case1 = ["ab","acb"]
print(isOneEditDistance(*case1))
# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.