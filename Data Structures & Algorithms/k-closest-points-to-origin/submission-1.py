import heapq

class Solution:
    def get_distance(self, x, y):
        return x ** 2 + y ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            distance = -self.get_distance(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (distance, x, y))
            elif distance > heap[0][0]:
                heapq.heapreplace(heap, (distance, x, y))
        
        return [[x, y] for d, x, y in heap]
        
