class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        
        for i in range(len(nums)):
            target = -nums[i]
            two_sum_result = self.two_sum(nums[i+1:], target)
            for two_sum_pair in two_sum_result:
                pair = (nums[i], two_sum_pair[0], two_sum_pair[1])
                res.add(tuple(sorted(pair)))

        return [list(t) for t in res]

    def two_sum(self, array, target):
        n = len(array)
        seen = set()
        res = set()
        for i in range(n):
            x = array[i]
            y = target - x
            if x in seen:
                pair = (x, y) if y >= x else (y, x)
                res.add(pair)

            seen.add(y)
        
        return res
        