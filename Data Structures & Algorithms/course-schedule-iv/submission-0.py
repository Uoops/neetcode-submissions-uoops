class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        result = []
        for u, v in queries:
            result.append(self.dfs(graph, set(), u, v))
        
        return result
    
    def dfs(self, graph, visited, start, end):
        if start == end:
            return True
        
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor in visited:
                return False
            
            if self.dfs(graph, visited, neighbor, end):
                return True
        return False