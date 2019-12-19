class WeightedEdge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight
    def __str__(self):
        return "({},{},{})".format(self.start,self.end,self.weight)
class Graph:
    def __init__(self,vertex_amount,edges):
        self.vertices = [i for i in range(vertex_amount)]
        self.edges = edges

def make_set(graph):
    return [float("-inf") for _ in range(len(graph.vertices))]

def union(x,y,mst):
    mst[y] = x
    return mst

def find(edge,mst):
    start_parent = edge.start
    end_parent = edge.end
    while mst[start_parent] != float("-inf"):
        start_parent = mst[start_parent] 
    while mst[end_parent] != float("-inf"):
        end_parent = mst[end_parent]
    return start_parent,end_parent 

def kruskals(graph):
    mst = make_set(graph)
    graph_edges = graph.edges
    graph_edges.sort(key=lambda x: x.start)
    graph_edges.sort(key=lambda x: x.weight)
    mst_edges = []
    i = 0
    while len(mst_edges) < len(graph.vertices)-1:
        cur_edge = graph_edges[i]
        start_parent,end_parent = find(cur_edge,mst) 
        if start_parent != end_parent:
            union(start_parent,end_parent,mst)
            mst_edges.append(cur_edge)
        i += 1
    return mst,mst_edges

if __name__ == "__main__":
    edges = [WeightedEdge(0,2,14),WeightedEdge(0,3,9),WeightedEdge(0,4,8),
        WeightedEdge(1,2,17),WeightedEdge(1,3,12),WeightedEdge(1,4,10),
        WeightedEdge(2,0,14),WeightedEdge(2,1,17),WeightedEdge(3,0,9),
        WeightedEdge(3,1,12),WeightedEdge(3,4,9),WeightedEdge(4,0,8),
        WeightedEdge(4,1,10),WeightedEdge(4,3,9)]
    graph = Graph(5,edges)
    answer = kruskals(graph)
    print("MST: ", answer[0])
    print("Edges: ", list(map(lambda x: str(x),answer[1])))
