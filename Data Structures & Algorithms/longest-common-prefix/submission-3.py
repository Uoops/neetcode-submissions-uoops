class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for word in strs[1:]:
                if i > len(word) - 1 or curr != word[i]:
                    return prefix
            
            prefix += curr
        
        return prefix