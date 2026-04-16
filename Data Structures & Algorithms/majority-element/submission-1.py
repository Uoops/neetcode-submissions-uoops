class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for x in nums:
            if candidate is None or count == 0:
                candidate = x
                count = 1
            elif candidate == x:
                count += 1
            else:
                count -= 1

        return candidate