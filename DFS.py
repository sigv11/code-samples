import sys
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Mark all nodes unvisited        
        self.visited = False  

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
	# For directed graph do not add this
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def getEdges(self):
        edges = []
	for currentVert in G:
		for nbr in currentVert.getConnections():
		    currentVertID = currentVert.getVertexID()
		    nbrID = nbr.getVertexID()
		    edges.append((currentVertID, nbrID, currentVert.getWeight(nbr)))
	return edges

    def printDot(self):
        print 'strict graph {'
        edges = self.getEdges()
        for edge in edges:
                print edge[0], '--', edge[1], '[key=1];'
        print '}'

def dfs(G, currentVert, visited):
    visited[currentVert] = True  # mark the visited node 
    print "traversal: " + currentVert.getVertexID()
    for nbr in currentVert.getConnections():  # take a neighbouring node 
        if nbr not in visited:  # condition to check whether the neighbour node is already visited
            dfs(G, nbr, visited)  # recursively traverse the neighbouring node 
 
def DFSTraversal(G):
    visited = {}  # Dictionary to mark the visited nodes 
    for currentVert in G:  # G contains vertex objects
        if currentVert not in visited:  # Start traversing from the root node only if its not visited 
            dfs(G, currentVert, visited)  # For a connected graph this is called only once 

if __name__ == '__main__':

    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addVertex('g')
    G.addVertex('h')
    G.addEdge('a', 'b', 1)  
    G.addEdge('b', 'c', 1)
    G.addEdge('b', 'h', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('e', 'h', 1)
    G.addEdge('e', 'f', 1)
    G.addEdge('e', 'g', 1)
 
    DFSTraversal(G)
    G.printDot()
