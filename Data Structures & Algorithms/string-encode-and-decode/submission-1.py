class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            start = i
            while s[start] != "#":
                start += 1
            
            length = 0
            for j in range(i, start):
                length = 10 * length + int(s[j])
            
            res.append(s[start + 1:start + 1 + length])
            i = start + 1 + length
        
        return res
