"""
    A python module to compute dijkstra's algorithm
    on a given weighted graph and prints out all
    the shortest paths from the input source node
    Author: Ian Gomez
    Github: imgomez0127
    Email: imgomez0127@gmail.com
"""
from dataclasses import dataclass, field
from heapq import heappop, heappush
@dataclass(order=True, unsafe_hash=True)
class Node:
    """
        A class to represent the nodes of the graph
        A wrapper used for comparison in the prioritu queue
    """

    distance: int
    label: int = field(compare=False)
    previous_node: int = field(compare=False)

class WeightedEdge:
    """
        A class to represent the weighted edges of the graph
        has a start node, end node, and weight
    """
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return "({},{},{})".format(self.start, self.end, self.weight)

class Graph:
    """
        A class to represent the graph which dijkstra's algorithm
        is performed on
    """
    @staticmethod
    def create_edges(nodes, edges):
        """
            A static method to create an adjacency list
            of edges between node labels and their adjacent nodes
        """
        edge_map = {node.label:[] for node in nodes}
        for edge in edges:
            edge_map[edge.start].append(edge)
        return edge_map

    def __init__(self, nodes, edges):
        self.nodes = [Node(float("inf"), i, -1) for i in range(nodes)]
        self.__edges = edges
        self.edges = Graph.create_edges(self.nodes, self.__edges)

    def __str__(self):
        return str(list(map(str, self.nodes))) + "\n" + str(list(map(str, self.__edges)))

def get_node(priority_queue, visited):
    """
        A function which returns the next non visited node
        in the priority queue
    """
    cur_node = heappop(priority_queue)
    while cur_node in visited:
        cur_node = heappop(priority_queue)
    return cur_node

def dijkstras(graph, source):
    """
        A function which performs dijkstra's
        single source shortest path algorithm.
        With inputs being an input graph and a number for
        the source node. It then returns the list of nodes it
        that it performed the algorithm on.
    """
    graph.nodes[source].distance = 0
    priority_queue = [graph.nodes[source]]
    visited = set()
    node_amount = len(graph.nodes)
    for _ in range(node_amount-1):
        cur_node = get_node(priority_queue, visited)
        visited.add(cur_node.label)
        for edge in graph.edges[cur_node.label]:
            if edge.end not in visited:
                distance = edge.weight + cur_node.distance
                if distance < graph.nodes[edge.end].distance:
                    graph.nodes[edge.end].distance = distance
                    graph.nodes[edge.end].previous_node = cur_node.label
                    heappush(priority_queue, graph.nodes[edge.end])
    return graph.nodes

def backtrack(graph, label):
    """
        A function which given an input graph that has had
        Dijkstra's algorithm applied to it will backtrack to
        display all paths with their lengths
    """
    nodes = graph.nodes
    cur_node = label
    backtrack_str = "{}".format(nodes[cur_node].label)
    while nodes[cur_node].previous_node != -1:
        cur_node = nodes[cur_node].previous_node
        backtrack_str = " -> " + backtrack_str
        backtrack_str = "{}".format(nodes[cur_node].label) + backtrack_str
    backtrack_str += " Distance: {}".format(nodes[label].distance)
    return backtrack_str

if __name__ == "__main__":
    EDGES = [WeightedEdge(0, 1, 3), WeightedEdge(0, 3, 7),
             WeightedEdge(1, 0, 3), WeightedEdge(1, 2, 4),
             WeightedEdge(1, 3, 2), WeightedEdge(2, 1, 4),
             WeightedEdge(2, 3, 5), WeightedEdge(2, 4, 6),
             WeightedEdge(3, 0, 7), WeightedEdge(3, 1, 4),
             WeightedEdge(3, 2, 5), WeightedEdge(3, 4, 4),
             WeightedEdge(4, 2, 6), WeightedEdge(4, 3, 4)]
    GRAPH = Graph(5, EDGES)
    X = dijkstras(GRAPH, 0)
    for node in GRAPH.nodes:
        print(backtrack(GRAPH, node.label))
