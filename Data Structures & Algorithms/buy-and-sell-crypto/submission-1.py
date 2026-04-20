class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for x in prices:
            res = max(res, x - min_price)
            min_price = min(min_price, x)
        
        return res
