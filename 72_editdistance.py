def minDistance(w1,w2):
    if w1 == w2: return 0
    min_operations = 0
    def recurse():
        nonlocal min_operations
        for i in 