class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
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

        while index + 1 < len(nums) and nums[index + 1] == nums[index]:
            index += 1
        
        self.dfs(index + 1, res, path, nums)
