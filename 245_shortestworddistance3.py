from typing import List

def shortestWordDistance(wordsDict: List[str], word1: str, word2: str) -> int:
    word1_index = -1
    word2_index = -1
    N = len(wordsDict)
    min_range = N
    for i in range(N):
        if wordsDict[i] == word1:
            word1_index = i
        if wordsDict[i] == word2 and i != word1_index:
            word2_index = i
        if word1_index != -1 and word2_index != -1:
            min_range = min(min_range, abs(word1_index - word2_index))
    return min_range

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
# Output: 3
case1 = [["practice", "makes", "perfect", "coding", "makes"],"makes","makes"]
print(shortestWordDistance(*case1))