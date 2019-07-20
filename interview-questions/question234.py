import numpy as np
def find_max_edge(graph,traversed):
    maximum_edge = 0
    node = -1
    root = -1
    for i in range(len(graph)):
        if traversed[i] == True: 
            for j,edge in enumerate(graph[i]):
                if edge > maximum_edge and not traversed[j]:
                    root = i
                    maximum_edge = edge
                    node = j
    return root,node

def all_traversed(traversed_list):
    all_edges_traversed = True
    for traversed_status in traversed_list:
        all_edges_traversed &= traversed_status
    return all_edges_traversed

def prims_algorithm(graph):
    edges = [False for _ in range(len(graph))]
    new_tree = [[0 for _ in range(len(graph))]
                for _ in range(len(graph))]
    edges[0] = True
    while not all_traversed(edges):
        current_edge,new_edge = find_max_edge(graph,edges)
        edges[new_edge] = True
        new_tree[current_edge][new_edge] = graph[current_edge][new_edge]
        new_tree[new_edge][current_edge] = graph[current_edge][new_edge]
    return new_tree
if __name__ == "__main__":
#    [[0,4,0,0,0,0,0,8,0],
#    [4,0,8,0,0,0,0,11,0],
#    [0,8,0
#    [0,0,7,0,9,14,0,0,0],
#    [0,0,0,9,0,10,0,0,0],
#    [0,0,4,14,10,0,2,0,0],
#    [0,0
    matrix = [[0,3,0,2,0,0,0,0,4],
            [3,0,0,0,0,0,0,4,0],
            [0,0,0,6,0,1,0,2,0],
            [2,0,6,0,1,0,0,0,0],
            [0,0,0,1,0,0,0,0,8],
            [0,0,1,0,0,0,8,0,0],
            [0,0,0,0,0,8,0,0,0],
            [0,4,2,0,0,0,0,0,0],
            [4,0,0,0,8,0,0,0,0],]
    print(prims_algorithm(matrix))
