class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]
        while left <= right:
            if height[left] <= height[right]:
                lmax = max(lmax, height[left])
                res += max(0, lmax - height[left])
                left += 1
            else:
                rmax = max(rmax, height[right])
                res += max(0, rmax - height[right])
                right -= 1

        return res                
