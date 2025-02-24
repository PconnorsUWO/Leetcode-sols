class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)
        
    def shortest(self, w1: str, w2: str) -> int:

        key = (w1, w2)
        if key in self.memoization:
            return self.memoization[key]
        if (w2, w1) in self.memoization:
            return self.memoization[(w2, w1)]
        
        w1i = -1
        w2i = -1
        wd = self.object_wordsdict
        min_dis = len(wd)
        for i in range(len(wd)):
            if wd[i] == w1:
                w1i = i
            if wd[i] == w2:
                w2i = i
            if w1i > -1 and w2i > -1:
                cur_dis = abs(w1i - w2i)
                min_dis = min(min_dis, cur_dis)
        
        self.memoization[key] = min_dis
        return min_dis