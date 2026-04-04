class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        path = []
        self.dfs(0, res, path, target, candidates)
        return res

    def dfs(self, index, res, path, remaining, candidates):
        if remaining == 0:
            res.append(path[:])
            return 
        
        if remaining < 0 or index == len(candidates):
            return 

        path.append(candidates[index])
        self.dfs(index + 1, res, path, remaining - candidates[index], candidates)
        path.pop()

        while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
            index += 1
        
        self.dfs(index + 1, res, path, remaining, candidates)