from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        majority_freq = 0
        res = 0
        for right in range(len(s)):
            char_in = s[right]
            count[char_in] += 1
            majority_freq = max(majority_freq, count[char_in])

            while (right - left + 1) - majority_freq > k:
                 char_out = s[left]
                 count[char_out] -= 1
                 left += 1
            
            res = max(res, right - left + 1)
        
        return res
