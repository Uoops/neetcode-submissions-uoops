from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        count = 0
        prefix_sum = 0
        for x in nums:
            prefix_sum += x
            count += prefix[prefix_sum - k]
            prefix[prefix_sum] += 1
        return count