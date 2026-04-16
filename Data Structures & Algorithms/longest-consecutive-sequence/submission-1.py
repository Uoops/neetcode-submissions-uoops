class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        array = set(nums)
        starts = []
        for x in array:
            if (x - 1) not in array:
                starts.append(x)

        longest = 0
        for start in starts:
            if (start - 1) in array:
                continue
                
            count = 1
            while (start + 1) in array:
                count += 1
                start += 1
            longest = max(longest, count)

        return longest