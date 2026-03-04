#Represent graph structures (adjacency list)
class Graph:
    def __init__(self):
        self.adjacency_list={}

    #vertex method 
    def add_vertex(self,vertex):
        self.adjacency_list[vertex] = []
    
    #add edges
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
    
    #implement BFS algorithm
    def bfs(self, start):
        visited={start}
        queue=[start]
        while queue:
            node = queue.pop(0)
            print(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)





#test if graph connection works
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
print(g.adjacency_list)
g.bfs("A")



