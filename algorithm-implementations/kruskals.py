class WeightedEdge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight
    def __str__(self):
        return "({},{},{})".format(self.start,self.end,self.weight)
class Graph:
    def __init__(vertex_amount,edges):
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
    graph_edges.sort(key=lambda x: x.weight)
    graph_edges.sort(key=lambda x: x.start)
    mst_edges = []
    i = 0
    while len(mst_edges) < len(graph.vertices)-1:
        cur_edge = graph_edges[i]
        start_parent,end_parent = find(cur_edge,mst) 
        if start_parent != end_parent:
            union(start_parent,end_parent,mst)
            mst_edges.append(cur_edge)
    return mst,mst_edges

