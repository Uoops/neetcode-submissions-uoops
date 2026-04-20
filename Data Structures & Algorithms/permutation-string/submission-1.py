from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        need = Counter(s1)
        window = Counter()
        missing = len(need)
        left = 0
        for right in range(n2):
            in_char = s2[right]
            window[in_char] += 1
            if window[in_char] == need[in_char]:
                missing -= 1
            
            if right - left + 1 > n1:
                out_char = s2[left]
                if window[out_char] == need[out_char]:
                    missing += 1
                window[out_char] -= 1
                left += 1

            if missing == 0:
                return True
        
        return False
