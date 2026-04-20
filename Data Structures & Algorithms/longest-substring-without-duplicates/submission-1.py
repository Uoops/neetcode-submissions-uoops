class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        left = 0
        for right in range(len(s)):
            curr = s[right]
            if curr in seen and seen[curr] >= left:
                left = seen[curr] + 1

            seen[curr] = right
            res = max(res, right - left + 1)
        
        return res