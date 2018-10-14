from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def bfs(self, source):
        visited = [False] * len(self.graph)
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            s = queue.pop(0)
            print(s)

            for vertex in self.graph[source]:
                if visited[vertex] == False:
                    queue.append(vertex)
                    visited[vertex] = True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(0)
