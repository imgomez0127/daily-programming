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
        i += 1
    return mst,mst_edges

if __name__ == "__main__":
    edges = [WeightedEdge(0,2,2), WeightedEdge(0,4,7), WeightedEdge(1,2,9), 
            WeightedEdge(1,3,9), WeightedEdge(2,0,2), WeightedEdge(2,1,9), 
            WeightedEdge(2,4,2), WeightedEdge(2,5,7), WeightedEdge(3,1,9), 
            WeightedEdge(3,5,5), WeightedEdge(4,0,7), WeightedEdge(4,2,2),
            WeightedEdge(5,2,7), WeightedEdge(5,3,5), WeightedEdge(5,6,3), 
            WeightedEdge(5,7,7), WeightedEdge(6,4,9), WeightedEdge(6,5,3),
            WeightedEdge(6,7,4), WeightedEdge(7,4,9), WeightedEdge(7,5,7), 
            WeightedEdge(7,6,4)]
    graph = Graph(7,edges)
    print(kruskals(graph))
