def maxSubstringLength(s: str, k: int) -> bool:
    if k == 0 or k == 1:
        return True
    
    res = []
    def backtrack(path):
        # return a set such that each subset in the set does not contain
        # an element of another subset i.e given A, B c U, A c B and B c A
        if path == k:
            res 