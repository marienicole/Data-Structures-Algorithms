from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def dfsutil(self, v, visited):
        visited[v] = True
        print(v,)

        for edge in self.graph[v]:
            if visited[edge] == False:
                self.dfsutil(edge, visited)

    def dfs(self, v):
        visited = [False] * len(self.graph)
        self.dfsutil(v, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs(0)
