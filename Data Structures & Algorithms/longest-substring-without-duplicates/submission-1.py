class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
            