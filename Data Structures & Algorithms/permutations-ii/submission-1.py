class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0, res, nums)
        return res

    def dfs(self, index, res, nums):
        if index == len(nums):
            res.append(nums[:])
            return

        visited = set()
        for i in range(index, len(nums)):
            if nums[i] in visited:
                continue

            visited.add(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            self.dfs(index + 1, res, nums)
            nums[index], nums[i] = nums[i], nums[index]