class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, val in enumerate(nums):
            if val in seen and abs(seen[val] - i) <= k:
                return True
            
            seen[val] = i
        
        return False
                
        