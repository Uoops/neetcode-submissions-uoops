from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        queue = deque()

        for val in arr:
            if len(queue) < k:
                queue.append(val)
            else:
                if abs(val - x) < abs(queue[0] - x):
                    queue.popleft()
                    queue.append(val)
        
        return list(queue)
