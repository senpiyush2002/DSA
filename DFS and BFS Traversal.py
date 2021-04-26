from collections import defaultdict
  
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
                                                                     # DFS Traversal
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # Main DFS Function
    def DFS(self, v): 
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
                                                                     # BFS Traversal    
    # BFS Function
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

 
 
#Construction of Graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

print ("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)

#   Output of DFS:
#   Following is DFS from (starting from vertex 2)
#   2 0 1 3



#   Output of BFS:
#   Following is Breadth First Traversal (starting from vertex 2)
#   2 0 3 1
