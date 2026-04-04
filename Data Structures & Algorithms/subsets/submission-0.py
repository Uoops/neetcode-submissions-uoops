class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.dfs(0, res, path, nums)
        return res
    
    def dfs(self, index, res, path, nums):
        if index == len(nums):
            res.append(path[:])
            return 

        path.append(nums[index])
        self.dfs(index + 1, res, path, nums)
        path.pop()

        self.dfs(index + 1, res, path, nums)