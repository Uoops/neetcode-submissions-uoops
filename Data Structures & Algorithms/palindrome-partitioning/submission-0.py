class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        self.dfs(0, path, res, s)
        return res

    def dfs(self, index, path, res, s):
        if index == len(s):
            res.append(path[:])
            return
        
        for i in range(index, len(s)):
            substring = s[index:i + 1]
            if self.is_palindrome(substring):
                path.append(substring)
                self.dfs(i + 1, path, res, s)
                path.pop()
    
    def is_palindrome(self, s):
        return s == s[::-1]