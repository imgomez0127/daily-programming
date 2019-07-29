"""
    Question asked by microsoft knowing what a minimum spanning tree is
    implement a maximum spanning tree (I accomplished this using prims
    algorithm however kruskals algorithm is another valid way to solve
    this question
    
    Prims algorithm but for maximum spanning tree:
        initialize and label all nodes from 1-n
        put the 0th node in the tree
        while not all nodes are in the tree:
            pick the lowest numbered node in the tree which has the highest weighted edge
            add the node to the tree 
    
    This implementation uses an adjacency matrix representation of the graph
    and the test matrix is from http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/weighted.html
"""            
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
