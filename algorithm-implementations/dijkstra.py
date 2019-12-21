from copy import copy
from dataclasses import dataclass, field
from heapq import heapify, heappop
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

class Graph:
    @staticmethod
    def create_edges(nodes,edges):
        edge_map = {node.label:[] for node in nodes}
        for edge in edges:
            edge_map[edge.start].append(edge)
        return edge_map 

    def __init__(self,nodes,edges):
        self.nodes = [Node(float("inf"),i,-1) for i in range(nodes)]
        self.edges = Graph.create_edges(nodes,edges)

def get_node(priority_queue,visited):
    cur_node = heappop(priority_queue)
    while(cur_node in visited):
        cur_node = heappop(priority_queue)
    return cur_node

def dijkstras(graph,source):
    graph.nodes[source].distance = 0 
    priority_queue = heapify([graph.nodes[source]])
    visited = set()
    node_amount = len(priority_queue)
    for _ in range(node_amount-1): 
        cur_node = get_node(priority_queue,visited)
        visited.add(cur_node.label)
        for edge in graph.edges[cur_node.label]:
            if edge.end not in visited:
                distance = edge.weight + cur_node.distance 
                if distance < graph.nodes[edge.end].distance:
                    graph.nodes[edge.end].distance = distance
    return graph.nodes 

if __name__ == "__main__":
    pass 
