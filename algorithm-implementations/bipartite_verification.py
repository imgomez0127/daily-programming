"""
   Name    : bipartite_verification.py
   Author  : Ian Gomez
   Date    : November 10, 2021
   Description :
   Github  : imgomez0127@github
"""
import enum
import collections


class Color(enum.Enum):

    NONE = 1
    RED = 2
    BLUE = 3


class Graph:

    def __init__(self, edges=None):
        self.edges = [] if not edges else edges
        self.colors = [Color.NONE] * len(self.edges)


def is_bipartite(graph):
    if not graph.edges:
        return True
    opposite_color = {
        Color.BLUE: Color.RED,
        Color.RED: Color.BLUE
    }
    graph.colors[0] = Color.BLUE
    q = collections.deque()
    q.append(0)
    while q:
        cur = q.popleft()
        for node in graph.edges[cur]:
            if graph.colors[node] == graph.colors[cur]:
                return False
            if graph.colors[node] == Color.NONE:
                graph.colors[node] = opposite_color[graph.colors[cur]]
                q.append(node)
    return True

hexagon_edges = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0]]
hexagon = Graph(edges=hexagon_edges)
triangle_edges = [[1, 2], [0, 2], [0, 1]]
triangle = Graph(edges=triangle_edges)
print(is_bipartite(hexagon))
print(hexagon.colors)
print(is_bipartite(triangle))
print(triangle.colors)
