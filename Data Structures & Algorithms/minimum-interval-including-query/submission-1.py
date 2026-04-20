import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_sorted = sorted(enumerate(queries), key=lambda x:x[1])
        result = [-1] * len(queries)
        heap = []
        i = 0

        for idx, val in queries_sorted:
            while i < len(intervals) and intervals[i][0] <= val:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1
            
            while heap and heap[0][1] < val:
                heapq.heappop(heap)
            
            if heap:
                result[idx] = heap[0][0]
        
        return result
