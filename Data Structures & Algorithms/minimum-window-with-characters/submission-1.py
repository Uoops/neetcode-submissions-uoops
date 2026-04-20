from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        missing = len(need)
        window = Counter()

        left = 0
        min_len = float('inf')
        min_start = 0

        for right in range(len(s)):
            in_char = s[right]
            window[in_char] += 1
            if in_char in need and window[in_char] == need[in_char]:
                missing -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                out_char = s[left]
                if out_char in need and window[out_char] == need[out_char]:
                    missing += 1
                window[out_char] -= 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
