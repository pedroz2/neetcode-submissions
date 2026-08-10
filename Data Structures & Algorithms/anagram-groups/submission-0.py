class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)
            if key not in anagrams: anagrams[key] = []
            anagrams[key].append(str)
        return list(anagrams.values())