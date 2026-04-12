class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        return self.dfs(graph, 0, -1, visited) and len(visited) == n

    def dfs(self, graph, node, parent, visited):
        if node in visited:
            return False

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if not self.dfs(graph, neighbor, node, visited):
                return False
        return True