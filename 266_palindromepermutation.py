from collections import Counter

def canPermutePalindrome(s: str) -> bool:
    count = Counter(s)
    N = len(s)
    if N % 2 == 0:
        for i in count.values():
            if i % 2 != 0: return False
        return True
    else:
        odd = 0
        for i in count.values():
            if i % 2 == 1: 
                odd += 1
                if odd > 1:
                    return False
        return True