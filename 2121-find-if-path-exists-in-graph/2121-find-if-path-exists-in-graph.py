class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for i in range(len(edges)):
            edge = edges[i]
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.dfs(graph, source, destination, visited)
        return visited[destination]

    def dfs(self, graph: List[List[int]], v: int, target: int, visited: List[bool]) -> bool:
        visited[v] = True
        for i in graph[v]:
            if i == target:
                visited[i] = True
                break
            if not visited[i]:
                self.dfs(graph, i, target, visited)