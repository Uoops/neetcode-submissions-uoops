class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        array = nums
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for x in array:
            if cand1 is not None and x == cand1:
                count1 += 1
            elif cand2 is not None and x == cand2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                cand1 = x
            elif count2 == 0:
                count2 = 1
                cand2 = x
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for x in array:
            if x == cand1:
                count1 += 1
            elif x == cand2:
                count2 += 1
        
        res = []
        n = len(array)
        if count1 > n // 3:
            res.append(cand1)
        if cand2 is not None and cand2 != cand1 and count2 > n // 3:
            res.append(cand2)
        
        return res