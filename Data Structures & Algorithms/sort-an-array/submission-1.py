class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return [nums[left]]
        
        mid = left + (right - left) // 2
        one = self.merge_sort(nums, left, mid)
        two = self.merge_sort(nums, mid + 1, right)
        return self.merger(one, two)
    
    def merger(self, one, two):
        i, j = 0, 0
        m, n = len(one), len(two)
        res = []
        while i < m and j < n:
            if one[i] <= two[j]:
                res.append(one[i])
                i += 1
            else:
                res.append(two[j])
                j += 1
        
        if i < m:
            res.extend(one[i:])
        if j < n:
            res.extend(two[j:])
        
        return res