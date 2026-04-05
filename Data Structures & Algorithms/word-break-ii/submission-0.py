class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        path = []
        self.dfs(0, res, path, s, wordDict)
        return res
    
    def dfs(self, index, res, path, s, wordDict):
        if index == len(s):
            res.append(' '.join(path))
            return

        for i in range(index, len(s)):
            substring = s[index:i + 1]
            if substring in wordDict:
                path.append(substring)
                self.dfs(i + 1, res, path, s, wordDict)
                path.pop()
