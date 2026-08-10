class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        freq = Counter(s1)
        for start in range(len(s2)):
            if Counter(s2[start:start+window]) == freq:
                return True
        return False