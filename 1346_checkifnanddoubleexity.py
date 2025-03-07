from typing import List
def checkIfExist(arr: List[int]) -> bool:   
    seen = set(arr)
    for i in arr:
        if i * 2 in seen or (i % 2 == 0 and i // 2 in seen):
            return True
    return False
