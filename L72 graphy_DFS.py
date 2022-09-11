class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
  
    def getVertices(self):                      # Get the keys of the dictionary
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    def findedges(self):                                   # Find the distinct list of edges
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
    def addVertex(self, vrtx):                 # Add the vertex as a key
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


    #递归DFS
    def depth_first_search(self,root=None):
        order=[]
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)
 
        if root:
            dfs(root)
 
        
        for node in self.nodes():                 #对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
            if not node in self.visited:
                dfs(node)
        self.visited = {}
        return order
 
    #非递归DFS
    def depth_first_search2(self,root=None):
        stack = []
        order = []
        #self.visited[root] = True
        def dfs():
            while stack:
                node = stack[-1]
                for n in self.node_neighbors[node]:
                    if not n in self.visited:
                        order.append(n)
                        stack.append(n)
                        self.visited[n] = True
                        break
                else:
                    stack.pop()
        if root:
            stack.append(root)
            order.append(root)
            self.visited[root]=True
            dfs()
 
        for node in self.nodes():
            if node not in self.visited:
                stack.append(node)
                order.append(node)
                self.visited[node]=True
                dfs()
 
        self.visited = {}
        return order
 
    def breadth_first_search(self,root=None):
        queue = []
        order = []
        def bfs():
            while len(queue)>0:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)
 
        if root:
            queue.append(root)
            order.append(root)
            bfs()
 
        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
 
        self.visited = {}
        return order

            

graph_elements = { "a" : ["b","c"],           # Create the dictionary with graph elements
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())
print(g.edges())
print(graph)
g.addVertex("f")
print(g)
g.addEdge({'a','e'})
g.addEdge({'a','c'})
print(g.getVertices())
print(g.edges())
















'''

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
'''
