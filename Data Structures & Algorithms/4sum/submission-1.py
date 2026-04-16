from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        seen = defaultdict(list)
        res = set()

        for j in range(1, n):
            for i in range(j):
                curr = nums[i] + nums[j]
                prev = target - curr
                if prev in seen:
                    for a, b in seen[prev]:
                        if b < i:
                            res.add((nums[a], nums[b], nums[i], nums[j]))

                seen[curr].append((i, j))

        return [list(p) for p in res]