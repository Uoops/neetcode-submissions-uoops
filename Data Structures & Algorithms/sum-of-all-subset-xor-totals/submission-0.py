class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = [0]
        self.dfs(0, 0, res, nums)
        return res[0]

    def dfs(self, index, path, res, nums):
        if index == len(nums):
            res[0] += path
            return 
        
        self.dfs(index + 1, path ^ nums[index], res, nums)
        self.dfs(index + 1, path, res, nums)
        
