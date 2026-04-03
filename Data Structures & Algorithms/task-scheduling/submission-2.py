from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        queue = deque()

        time = 0
        while heap or queue:
            time += 1

            if queue and queue[0][0] == time:
                _, freq = queue.popleft()
                heapq.heappush(heap, freq)
            if heap:
                freq = heapq.heappop(heap) + 1
                if freq != 0:
                    queue.append((time + n + 1, freq))


        return time
