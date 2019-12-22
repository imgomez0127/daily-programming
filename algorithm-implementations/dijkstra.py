from copy import copy
from dataclasses import dataclass, field
from heapq import heapify, heappop, heappush
@dataclass(order=True,unsafe_hash=True)
class Node:
    distance: int
    label: int=field(compare=False)
    previous_node: int=field(compare=False) 

class WeightedEdge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return "({},{},{})".format(self.start,self.end,self.weight)

class Graph:
    @staticmethod
    def create_edges(nodes,edges):
        edge_map = {node.label:[] for node in nodes}
        for edge in edges:
            edge_map[edge.start].append(edge)
        return edge_map 

    def __init__(self,nodes,edges):
        self.nodes = [Node(float("inf"),i,-1) for i in range(nodes)]
        self.__edges = edges
        self.edges = Graph.create_edges(self.nodes,self.__edges)

    def __str__(self):
        return str(list(map(lambda x: str(x), self.nodes))) + "\n" + str(list(map(lambda x: str(x), self.__edges)))

def get_node(priority_queue,visited):
    cur_node = heappop(priority_queue)
    while(cur_node in visited):
        cur_node = heappop(priority_queue)
    return cur_node

def dijkstras(graph,source):
    graph.nodes[source].distance = 0 
    priority_queue = [graph.nodes[source]]
    visited = set()
    node_amount = len(graph.nodes)
    for _ in range(node_amount-1): 
        cur_node = get_node(priority_queue,visited)
        visited.add(cur_node.label)
        for edge in graph.edges[cur_node.label]:
            if edge.end not in visited:
                distance = edge.weight + cur_node.distance 
                if distance < graph.nodes[edge.end].distance:
                    graph.nodes[edge.end].distance = distance 
                    graph.nodes[edge.end].previous_node = cur_node.label
                    heappush(priority_queue,graph.nodes[edge.end])
    return graph.nodes 

if __name__ == "__main__":
    edges = [WeightedEdge(0,1,3),WeightedEdge(0,3,7),
            WeightedEdge(1,0,3),WeightedEdge(1,2,4),WeightedEdge(1,3,2),
            WeightedEdge(2,1,4),WeightedEdge(2,3,5),WeightedEdge(2,4,6),
            WeightedEdge(3,0,7),WeightedEdge(3,1,4),WeightedEdge(3,2,5),
            WeightedEdge(3,4,4),WeightedEdge(4,2,6),WeightedEdge(4,3,4)]
    graph = Graph(5,edges)  
    print(graph) 
    x = dijkstras(graph,0)
    print(x)
