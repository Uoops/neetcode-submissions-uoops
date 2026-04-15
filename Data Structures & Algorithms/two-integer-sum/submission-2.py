class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i, val in enumerate(nums):
            if val in seen:
                res.append(seen[val])
                res.append(i)
            seen[target-val] = i

        return res
        